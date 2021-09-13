from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    # db_index= True, indexing the SQL name -- faster search
    slug = models.SlugField(max_length=255, unique=True)
    # unique = True, no two slugs can be the same
    class Meta:
        verbose_name_plural = 'categories'
        # verbose name changes the admin panel naming of Category ( default just adds 's' at the end)
    
    def get_absolute_url(self):
        return reverse('bookstore:category_list', args=[self.slug])
        # bookstore refers to app_name in urls, category_list is name of a url path 
        # args = [self.slug] slug of whatever item we are trying to view
        # this will build us the URL so we can now use the function dinamicly  {{ category.get_absolute_url}}

    def __str__(self):
        return self.name


class Books(models.Model):
    category = models.ForeignKey(Category, related_name='item', on_delete=models.CASCADE)
    # we want the information to come from Category model so we are building a link with that table with a Foreign Key
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='item_creator')
    # creating a link just like with category, but instead of category the link is with User
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='admin')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/') 
    # django will create images folder in our media folder automatically
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Books'
        ordering = ('-created',)
        # when we return all data from a product, we define how we will order it with "ordering = -created"

    def get_absolute_url(self):
        return reverse('bookstore:book_detail', args=[self.slug])
        # bookstore refers to app_name in urls, product_detail is name of a url path 
        # args = [self.slug] slug of whatever item we are trying to view
        # this will build us the URL so we can now use the function dinamicly  {{ product.get_absolute_url}}

    def __str__(self):
        return self.title
    
