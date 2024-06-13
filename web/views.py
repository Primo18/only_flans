from django.shortcuts import render, get_object_or_404, redirect
from .models import Flan
from .forms import ContactFormForm
from unidecode import unidecode
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from .forms import RegisterForm


def register(request):
    if request.user.is_authenticated:
        return redirect("index")
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
    else:
        form = RegisterForm()
    return render(request, "web/register.html", {"form": form})


class CustomLoginView(LoginView):
    template_name = "web/login.html"
    redirect_authenticated_user = True


def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(request, "web/index.html", {"flanes": flanes_publicos})


def about(request):
    return render(request, "web/about.html")


@login_required
def welcome(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    return render(request, "web/welcome.html", {"flanes": flanes_privados})


def flan_detail(request, slug):
    flan = get_object_or_404(Flan, slug=slug)
    return render(request, "web/flan_detail.html", {"flan": flan})


@require_POST
def toggle_privacy(request, slug):
    flan = get_object_or_404(Flan, slug=slug)
    flan.is_private = not flan.is_private
    flan.save()
    return redirect("flan_detail", slug=flan.slug)


@require_POST
def buy_flan(request, slug):
    flan = get_object_or_404(Flan, slug=slug)
    # Aquí puedes añadir la lógica para manejar la compra
    return redirect("flan_detail", slug=flan.slug)


def contact(request):
    if request.method == "POST":
        form = ContactFormForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("contact_success")
    else:
        form = ContactFormForm()
    return render(request, "web/contact.html", {"form": form})


def contact_success(request):
    return render(request, "web/contact_success.html")


def search(request):
    query = request.GET.get("q", "").strip()
    if query:
        normalized_query = unidecode(query).lower()
        flanes = Flan.objects.filter(normalized_name__icontains=normalized_query)
    else:
        flanes = Flan.objects.all()
    return render(
        request, "web/search_results.html", {"flanes": flanes, "query": query}
    )
