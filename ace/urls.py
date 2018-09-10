from django.contrib import admin
from django.urls import path, include

from website.views import index, magazine

urlpatterns = [
    path('admin/', admin.site.urls),
    path('magazine/', magazine, name='magazine'),

    # path('s3direct/', include('s3direct.urls')),
    path('portal/', include('portalapp.urls')),
    path('', include('website.urls')),
    path('', include('social_django.urls', namespace='social'))

]

admin.site.site_header = 'ACE'

handler404 = 'website.views.view_404'
