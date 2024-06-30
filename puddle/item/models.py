from django.contrib.auth.models import User
from django.db import models
#this is a table that will be created in the database
class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

#this is a table that will be created in the database
class Item(models.Model): # this is the item model
    Category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE) # this is the category of the item, also gets the items that belongs to the specific category, and when the category is deleted, the items will also be deleted, this is the relationship between the category and the item
    name = models.CharField(max_length=255) # this is the name of the item
    description = models.TextField(blank=True, null=True) # this is the description of the item
    price = models.FloatField() # this is the price of the item
    image = models.ImageField(upload_to='item_images', blank=True, null=True) # this is the image of the item
    is_sold = models.BooleanField(default=False) # this is the status of the item
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE) #this is the user who created the item, also gets the items that belongs to the specific user, and when the user is deleted, the items will also be deleted, this is the relationship between the user and the item
    created_at = models.DateTimeField(auto_now_add=True) # this is the date and time the item was created

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name