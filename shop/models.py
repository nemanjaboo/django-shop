from django.db import models
from django.utils.text import slugify
from datetime import date
from django.urls import reverse
from django.contrib.auth.models import User
from django.dispatch import receiver 
from django.db.models.signals import post_save
from django.conf import settings


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

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorites = models.ManyToManyField(Game)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
    
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)

class Favorite(models.Model):
    profile = models.ManyToManyField(Profile)
    game = models.ManyToManyField(Game)
    time = models.DateTimeField(auto_now_add=True)

    #Pivot tabela
    # Pogledaj foreign key i through 