from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from django.conf import settings

from website.views import index, magazine

urlpatterns = [
    path('', index),
    path('magazine/', magazine),
    path('admin/', admin.site.urls),
    path('s3direct/', include('s3direct.urls')),
    path('portal/', include('portalapp.urls')),
    path('filer/', include('filer.urls')),
    path('', include('social_django.urls', namespace='social'))

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
admin.site.site_header = 'ACE'

handler404 = 'website.views.view_404'
