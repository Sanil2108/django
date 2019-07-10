from django.db import models

class User(models.Model):
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100, primary_key = True)
    password = models.CharField(max_length = 20)

    def __str__(self):
        return self.name + ', ' + self.email