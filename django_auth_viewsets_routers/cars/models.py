from django.db import models

class Car(models.Model):
    name = models.CharField(max_length = 100)
    year = models.IntegerField()

    def __str__(self):
        return '{} of the year {}'.format(self.name, self.year)

class Engine(models.Model):
    installed_in = models.ManyToManyField(Car)
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name