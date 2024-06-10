from django.contrib import admin
from .models import Flan
from .models import ContactForm


@admin.register(Flan)
class FlanAdmin(admin.ModelAdmin):
    list_display = ("name", "is_private", "slug")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ("customer_name", "customer_email", "message")
