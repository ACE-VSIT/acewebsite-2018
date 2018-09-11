from django.urls import path
from portalapp import views

urlpatterns = [
    path('', views.login, name='login'),
    path('home/', views.home, name='portal'),
    path('submission/', views.submit_task, name='submit_task'),
    path('form/', views.form_data, name='form_data'),
    path('success/', views.form_input, name='form_input'),
]
