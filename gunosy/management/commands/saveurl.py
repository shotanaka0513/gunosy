from django.core.management.base import BaseCommand
import crawler.gettrain
import classifier.naivebayes

class Command(BaseCommand):

	def handle(self, *args, **options):
		nb = classifier.naivebayes.NaiveBayes()
		crawler.gettrain.gunosy_train(nb)
