import debug_toolbar
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('page/', include('django.contrib.flatpages.urls')),
    path('admin/', admin.site.urls),
    # accounts
    path('accounts/', include('allauth.urls')),
    # main
    path('chat/', include('chatbot.urls')),
    path('', include('main.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
]
