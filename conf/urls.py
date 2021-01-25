from django.contrib import admin
from django.urls import include, path


from main.views import index

urlpatterns = [
    path('admin/', admin.site.urls),

    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('page/', include('django.contrib.flatpages.urls')),
    path('', index, name='index')
    
]
