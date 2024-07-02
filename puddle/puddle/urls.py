from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('', include('core.urls')), # this will include the urls from the core app
    path('item/', include('item.urls')), # this will include the urls from the item app
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
