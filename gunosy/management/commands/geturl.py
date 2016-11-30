from django.core.management.base import BaseCommand
from crawler import geturl


class Command(BaseCommand):

    def handle(self, *args, **options):
        geturl.get_url()
