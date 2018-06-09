from django.urls import path

from . import views

app_name = 'tdlist'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:person_id>/bump/', views.bump, name='bump'),

]