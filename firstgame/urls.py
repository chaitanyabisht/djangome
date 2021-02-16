from django.urls import path

from firstgame import views

urlpatterns = [
    path('', views.firstgame, name="firstgame"),
    path('hobbies/', views.hobbies, name='hobbies')
]