from django.db import models

class Article(models.Model):
    title = models.CharField(max_length = 100)
    reading_time = models.IntegerField()
    author_name = models.CharField(max_length = 100)

    def __str__(self):
        return '{title} by {author}'.format(title = self.title, author = self.author_name)

class User(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    age = models.IntegerField()
    