from django.urls import path
from . import views


urlpatterns = [
    path('', views.index,name='home'),
    path('login_test/', views.login_test)
]
