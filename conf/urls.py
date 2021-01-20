from django.contrib import admin
from django.urls import include, path
from django.contrib.flatpages import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('django.contrib.flatpages.urls')),
]
