from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from website.views import index, magazine,projects

urlpatterns = [
    path('', index),
    
    path('admin/', admin.site.urls),
    #path('s3direct/', include('s3direct.urls')),
    path('portal/', include('portalapp.urls')),
    path(r'', include('website.urls')),
    path('', include('social_django.urls', namespace='social'))


]

admin.site.site_header = 'ACE'

handler404 = 'website.views.view_404'
