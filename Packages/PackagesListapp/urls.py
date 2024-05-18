from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePages , name = 'HomePages'),
    path('register', views.Register, name = 'register'),
    path('login', views.Login, name = 'login'),
    path('show_data', views.ShowData, name='show_data'),
]
