from django.db import models

L_CHOICES = [
  ('1', '1styear'),
  ('2', '2ndyear'),
  ('3', '3rdyear'),
  ('4', '4thyear'),
]

class Student(models.Model):
  name = models.CharField(primary_key = True, max_length = 255,)
  level = models.CharField(max_length = 2, choices = L_CHOICES)