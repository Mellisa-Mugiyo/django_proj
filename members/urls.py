from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'members'

urlpatterns = [
    path('register/',views.register,name = 'register'),
    path('user/',views.userhome,name = 'userhome'),
    path('userpage/',views.userpage,name = 'userpage'),
    path('login/', auth_views.LoginView.as_view(template_name = 'authenticate/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),

]

 