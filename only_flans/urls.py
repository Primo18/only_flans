from django.contrib import admin
from django.urls import path
from web.views import index, about, contact, welcome

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("welcome/", welcome, name="welcome"),
]
