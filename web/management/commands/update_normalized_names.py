from django.core.management.base import BaseCommand
from web.models import Flan
from unidecode import unidecode


class Command(BaseCommand):
    help = "Update normalized_name field for existing flans"

    def handle(self, *args, **kwargs):
        flanes = Flan.objects.all()
        for flan in flanes:
            flan.normalized_name = unidecode(flan.name).lower()
            flan.save()
        self.stdout.write(
            self.style.SUCCESS("Successfully updated normalized_name for all flans")
        )
