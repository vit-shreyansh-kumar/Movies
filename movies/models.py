from django.db import models

__all__ = ['Certificate',
           'Country',
           'Language',
           'Genres',
           'Actor',
           'Movie']

# Create your models here.


class Certificate(models.Model):
    type = models.CharField(max_length=20,null=False)

    def __str__(self):
        return str(self.type)


class Country(models.Model):
    name = models.CharField(max_length=100,null=False,blank=False,unique=True)

    def __str__(self):
        return str(self.name)


class Language(models.Model):
    name = models.CharField(max_length=100,null=False,blank=False)

    def __str__(self):
        return str(self.name)


class Genres(models.Model):
    name = models.CharField(max_length=40,null=False,blank=False)

    def __str__(self):
        return str(self.name)


class Actor(models.Model):
    fname = models.CharField(max_length=40,null=False,blank=False)
    lname = models.CharField(max_length=40)

    def __str__(self):
        return str(self.fname+" "+self.lname)


class Movie(models.Model):
    name = models.CharField(max_length=100,null=False,blank=False)
    storyline = models.TextField(max_length=300,blank=True,null=True)
    genres = models.ManyToManyField(Genres)
    certificate = models.ForeignKey(Certificate)
    country = models.ForeignKey(Country)
    language = models.ForeignKey(Language)
    budget = models.CharField(max_length=50,null=True,blank=True)
    actor = models.ManyToManyField(Actor,related_name="actor_name")
    director = models.ManyToManyField(Actor,related_name="director_name")
    score = models.FloatField(max_length=3)

    def __str__(self):
        return str(self.name)
