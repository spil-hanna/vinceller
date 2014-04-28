from django.db import models

NAME_LENGTH = 100
URL_LENGTH = 200

class Grape(models.Model):
    name = models.CharField(max_length=NAME_LENGTH)
    description = models.TextField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=NAME_LENGTH)
    description = models.TextField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    # TODO: add geolocation/google map link, etc

    def __str__(self):
        return self.name


class Winery(models.Model):
    name = models.CharField(max_length=NAME_LENGTH)
    region = models.ForeignKey(Region, blank=True, null=True)
    website = models.CharField(max_length=URL_LENGTH, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    # TODO: add geolocation/google map link, etc

    def __str__(self):
        return self.name


class Year(models.Model):
    year = models.IntegerField()
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.year)


class Wine(models.Model):
    name = models.CharField(max_length=NAME_LENGTH)
    year = models.ForeignKey(Year)
    grapes = models.ManyToManyField(Grape, blank=True, null=True)
    region = models.ForeignKey(Region, blank=True, null=True)
    winery = models.ForeignKey(Winery, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    photo_uri = models.CharField(max_length=URL_LENGTH, blank=True, null=True)

    def __str__(self):
        return self.name


class Purchase(models.Model):
    wine = models.ForeignKey(Wine)
    date = models.DateField()
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return 'purchase {0} on {1}'.format(self.wine.name, self.date)


class Tasting(models.Model):
    wine = models.ForeignKey(Wine)
    date = models.DateField()
    RATING = (
        ('1', 'felejtos'),
        ('2', 'okes'),
        ('3', 'jobbacska'),
        ('4', 'unneplos'),
        ('5', 'vilagformalos'),
    )
    rating = models.CharField(max_length=1, choices=RATING)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return 'tasting {0} on {1}'.format(self.wine.name, self.date)


