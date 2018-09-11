from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', views.logout, name='logout'),
    path('members/', views.member, name='members'),
    path('events/', views.event, name='events'),
    path('projects/', views.project, name='projects'),
    path('gallery/', views.gallery, name='gallery'),
    path('achievements/', views.achievement, name='achievements'),
    path('calendar/', views.agenda, name='calendar'),
    path('mentors/', views.mentor, name='mentors'),
    path('alumnus/', views.alumni, name='alumnus'),
    path('code-of-conduct/', views.codeofconduct, name='code_of_conduct'),
    path('selection-procedure/', views.selection, name='selection_procedure'),
]
