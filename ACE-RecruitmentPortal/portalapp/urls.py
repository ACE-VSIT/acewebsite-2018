from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ace_website, name='ace_website'),
    url(r'^portal/$', views.login, name='login'),
    url(r'^home/$', views.home, name='home'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^submission/$', views.submit_task, name='submit_task'), 
    url(r'^form/$', views.form_data, name='form_data'),
    url(r'^success/$', views.form_input, name='form_input'),
    url(r'^acem2017/$', views.ace_magazine, name='ace_magazine'),
    url(r'^ACE-DontBlink/$',views.ace_video,name='ace_video'),
    url(r'^908978972686767575675675/$', views.serve_main_page, name='serve_main_page')
]

