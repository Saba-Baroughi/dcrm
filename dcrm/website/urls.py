
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login_user, name='login'),
    #This path is when you want to create login page in another page
    path('logout/', views.logout_user, name='logout'),
   
]
