from django.core.management.base import BaseCommand
from crawler import gettrain


class Command(BaseCommand):

    def handle(self, *args, **options):
        gettrain.get_train()
