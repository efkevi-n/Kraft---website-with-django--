
from django.urls import path

from .views import detail # this imports the detail view from the views.py file
from . import views
app_name = 'item' #this is the namespace for the item app

urlpatterns = [
    path('<int:pk>/', views.detail, name='detail'),    # this is the detail view that will render the detail.html template for each item
]