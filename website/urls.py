from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('members/', views.member, name='member'),
    path('events/', views.event, name='events'),
    path('projects/', views.project, name='projects'),
    path('gallery/', views.gallery, name='gallery'),
    path('achievments/', views.achievement, name='achievment'),
    path('calender/', views.calender, name='calender'),
    path('mentor/', views.mentor, name='mentor'),
    path('alumni/', views.alumni, name='alumni'),
    path('codeofconduct/', views.codeofconduct, name='magazine'),
    path('selection/', views.selection, name='magazine'),
]
