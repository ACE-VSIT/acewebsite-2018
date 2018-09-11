from django.urls import path
from library import views

urlpatterns = [
    path('', views.index, name='library_index'),
    path('assignments/', views.assignment, name='assignments'),
    path('resources/$', views.resources, name='resource'),
    path('resource/(?P<pk>[\w\-]+)/$', views.resource_details, name='resource_details'),

    # TODO : Add routes for other pages
]
