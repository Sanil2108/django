from django.db import models

class Contact(models.Model):
    contact_name = models.CharField("Name", max_length = 100)
    phone = models.CharField("Phone number", max_length = 20)
    email = models.CharField("Email address", max_length= 200)

    def __str__(self):
        return contact_name
