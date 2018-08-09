from django.urls import path, include
from portalapp import views

urlpatterns = [
    path('', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('logout', views.logout, name='logout'),
    path('submission/', views.submit_task, name='submit_task'),
    path('form/', views.form_data, name='form_data'),
    path('success/', views.form_input, name='form_input'),
    # path('acem2017/$', views.ace_magazine, name='ace_magazine'),
    # path('ACE-DontBlink/$', views.ace_video, name='ace_video'),
    # path('908978972686767575675675/$', views.serve_main_page, name='serve_main_page')
]
