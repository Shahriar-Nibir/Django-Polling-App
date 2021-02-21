from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.loginProc, name='login'),
    path('signup', views.signup, name='signup'),
    path('poll/<str:pk>', views.poll, name='poll'),
    path('confirm/<str:pk>', views.confirm, name='confirm')
]
