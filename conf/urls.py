# import debug_toolbar
from django.contrib import admin
from django.urls import include, path, re_path


from main.views import AdvertViewSet


urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('page/', include('django.contrib.flatpages.urls')),
    path('admin/', admin.site.urls),
    # API
    re_path('^api/v1/adverts/(?P<query>.+)/$', AdvertViewSet.as_view()),
    path('api/v1/adverts/', AdvertViewSet.as_view()),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # accounts
    path('accounts/', include('allauth.urls')),
    # main
    path('chat/', include('chatbot.urls')),
    path('', include('main.urls')),
    # path('__debug__/', include(debug_toolbar.urls)),
]
