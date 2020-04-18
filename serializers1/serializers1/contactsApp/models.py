from django.db import models

class User(models.Model):
    name = models.CharField(max_length = 120)
    email = models.EmailField()
    age = models.IntegerField()

class Engine(models.Model):
    make = models.CharField(max_length = 100)
    year = models.IntegerField()

    def __str__(self):
        return self.make + ' of the year ' + str(self.year)

class Car(models.Model):
    name = models.CharField(max_length = 100)
    make = models.IntegerField()
    # Many to many field
    engines = models.ManyToManyField(Engine)
    # One to many relationship
    # engine = models.ForeignKey(Engine, on_delete = models.CASCADE)

    def __str__(self):
        return self.name + ' of the year ' + str(self.make)
    