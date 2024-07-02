from django.shortcuts import render

from item.models import Item, Category # this is the item model and the category model

from .forms import CreateUserForm # this is the form that will be used to create a new user

def index(request):
    items = Item.objects.filter(is_sold=False) # this will get all the items that are not sold from the database
    categories = Category.objects.all() # this will get all the categories from the database
    return render(request, 'core/index.html', {'items': items, 'categories': categories}) # this is the index view that will render the index.html template and pass the items and categories to the template

def contact(request):

    return render(request, 'core/contact.html')

def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CreateUserForm()
    return render(request, 'core/signup.html', {'form': form}) # this is the register view that will render the register.html template and pass the form to the template