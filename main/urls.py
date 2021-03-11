from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.loginProc, name='login'),
    path('signup', views.signup, name='signup'),
    path('poll/<str:pk>', views.poll, name='poll'),
    path('confirm/<str:pk>', views.confirm, name='confirm'),
    path('group', views.group, name='group'),
    path('createpoll', views.createpoll, name='createpoll'),
    path('addoptions/<str:pk>', views.addoptions, name='addoptions'),
    path('result/<str:pk>', views.result, name='result'),
    path('logoutUser', views.logoutUser, name='logoutUser'),
    path('updatepoll/<str:pk>', views.updatepoll, name='updatepoll'),
    path('deletepoll/<str:pk>', views.deletepoll, name='deletepoll')
]
