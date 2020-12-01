from django.urls import path

from . import views

app_name = 'interface'

# index page
urlpatterns = [
    path('', views.index, name='index'),
]
