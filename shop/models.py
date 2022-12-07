from django.db import models
from django.utils.text import slugify
from datetime import date
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Game(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    price = models.IntegerField()
    status = models.BooleanField(default=0)
    # image = models.ImageField(upload_to='gameimages/', null=True)
    image = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Game, self).save(*args, **kwargs)

    def get_absoulte_url(self):
        return reverse("shop:game-detail", kwargs={"slug": self.slug})
