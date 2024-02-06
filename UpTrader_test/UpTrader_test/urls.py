
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('', include('menu.urls')),
    path('admin/', admin.site.urls),
]
