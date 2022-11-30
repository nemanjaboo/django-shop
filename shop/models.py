from django.db import models
from django.utils.text import slugify

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Game(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=7)
    category = models.ManyToManyField(Category)
    status = models.BooleanField(default=0)
    players = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Game, self).save(*args, **kwargs)
