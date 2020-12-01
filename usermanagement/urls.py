from django.urls import path

from . import views

app_name = 'usermanagement'
urlpatterns = [
    path('users', views.users_index, name='users_index'),
    path('users/register',views.register,name='register'),
    path('users/login',views.user_login,name='user_login'),
    path('users/logout',views.user_logout,name='user_logout'),

]
