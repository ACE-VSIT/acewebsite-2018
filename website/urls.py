from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('members/', views.member, name='members'),
    path('events/', views.event, name='events'),
    path('projects/', views.project, name='projects'),
    path('gallery/', views.gallery, name='gallery'),
    path('achievements/', views.achievement, name='achievements'),
    path('calendar/', views.agenda, name='calendar'),
    path('magazine/', views.magazine, name='magazine'),
    path('mentor/', views.mentor, name='mentor'),
    path('alumni/', views.alumni, name='alumni'),
]
