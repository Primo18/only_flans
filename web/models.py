from django.db import models
from unidecode import unidecode
import uuid


class Flan(models.Model):
    flan_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=64)
    normalized_name = models.CharField(max_length=64, editable=False)
    description = models.TextField()
    image_url = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    is_private = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.normalized_name = unidecode(self.name).lower()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True
    )
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()

    def __str__(self):
        return self.customer_name
