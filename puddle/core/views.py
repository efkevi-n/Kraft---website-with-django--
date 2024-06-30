from django.shortcuts import render

from item.models import Item, Category # this is the item model and the category model

def index(request):
    items = Item.objects.filter(is_sold=False) # this will get all the items that are not sold from the database
    categories = Category.objects.all() # this will get all the categories from the database
    return render(request, 'core/index.html', {'items': items, 'categories': categories}) # this is the index view that will render the index.html template and pass the items and categories to the template

def contact(request):

    return render(request, 'core/contact.html')
