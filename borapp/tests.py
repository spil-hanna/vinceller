from django.test import TestCase

from borapp.models import *

class GrapeTest(TestCase):
    def test_str(self):
        grape = Grape.objects.create(name='Cabernet Sauvignon')

class RegionTest(TestCase):
    def test_str(self):
        region = Region.objects.create(name='Eger')

class WineryTest(TestCase):
    def test_str(self):
        region = Region(name='Eger')
        region.save()
        winery = Winery.objects.create(name='Simon', region=region)

        self.assertEquals(len(Winery.objects.all()), 1)




