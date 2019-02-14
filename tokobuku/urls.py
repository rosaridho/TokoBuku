from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home.urls')),
    path('kategori/', include('Kategori.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$',
        serve, {'document_root': settings.MEDIA_ROOT, }),]