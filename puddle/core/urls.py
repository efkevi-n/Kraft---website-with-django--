from django.urls import path # this imports the path function from django

from  . import views # this imports the views from the current directory

app_name = 'core' #this is the namespace for the core app , we will use this to refer to the core app in the templates

urlpatterns = [ # this is the list of urls for the core app
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
]