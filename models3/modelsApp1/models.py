from django.db import models

DINOSAUR_SPECIES_CHOICES = [
  ('TREX', 't'),
  ('TREX ka bhai', 'tb'),
  ('TREX ki mom', 'tm'),
  ('TREX ke dad', 'td'),
  ('TREX ki behen', 'tbehen'),
]

class Dinosaur(models.Model):
  species = models.CharField(max_length = 100, choices = DINOSAUR_SPECIES_CHOICES)
  name = models.CharField(max_length = 100)

class AuthorModelManager(models.Manager):
  def first_name_keyword_count(self, first_name_keyword):
    return self.filter(first_name__contains = first_name_keyword).count()

class Publisher(models.Model):
  name = models.CharField(max_length = 100)
  country = models.CharField(max_length = 100)
  website = models.URLField()

  def __unicode__(self):
    return '{name} from {country}'.format(name = self.name, country = self.country)

class Author(models.Model):
  first_name = models.CharField(max_length = 100)
  last_name = models.CharField(max_length = 100)
  email = models.EmailField()

  objects = AuthorModelManager()

  def __unicode__(self):
    return '{fname} {lname}'.format(fname = self.first_name, lname = self.last_name)

class Book(models.Model):
  title = models.CharField(max_length = 100)
  authors = models.ManyToManyField(Author)
  publisher = models.ForeignKey(Publisher, on_delete = models.CASCADE)

  def __unicode__(self):
    authors_string = ''
    for author in self.authors:
      authors_string += str(author) + ', '
    return '{title} by {authors_string}'.format(title = self.title, authors_string = authors_string)