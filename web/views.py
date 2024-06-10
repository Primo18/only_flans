from django.shortcuts import render, get_object_or_404, redirect
from .models import Flan
from .forms import ContactFormForm
from unidecode import unidecode
from django.views.decorators.http import require_POST


def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(request, "web/index.html", {"flanes": flanes_publicos})


def about(request):
    return render(request, "web/about.html")


def contact(request):
    return render(request, "web/contact.html")


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
    return redirect(
        "flan_detail", slug=flan.slug
    )  # Redirecciona usando el nombre de la vista


@require_POST
def buy_flan(request, slug):
    # Lógica para comprar el flan (por ejemplo, agregar a un carrito de compras)
    flan = get_object_or_404(Flan, slug=slug)
    # Aquí puedes añadir la lógica para manejar la compra
    return redirect(
        "flan_detail", slug=flan.slug
    )  # Redirecciona usando el nombre de la vista


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
    query = request.GET.get("q", "")
    if query:
        flanes = Flan.objects.filter(name__icontains=query)
    else:
        flanes = Flan.objects.all()
    return render(
        request, "web/search_results.html", {"flanes": flanes, "query": query}
    )


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
