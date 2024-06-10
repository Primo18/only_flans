from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from web.views import (
    index,
    about,
    contact,
    welcome,
    flan_detail,
    toggle_privacy,
    buy_flan,
    contact_success,
    search,
)

urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("search/", search, name="search"),
    path("contact/success/", contact_success, name="contact_success"),
    path("welcome/", welcome, name="welcome"),
    path("flan/<slug:slug>/", flan_detail, name="flan_detail"),
    path("flan/<slug:slug>/toggle_privacy/", toggle_privacy, name="toggle_privacy"),
    path("flan/<slug:slug>/buy/", buy_flan, name="buy_flan"),
]


urlpatterns += i18n_patterns(
    path("admin/", admin.site.urls),
)
