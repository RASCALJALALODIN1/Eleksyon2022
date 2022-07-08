from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.Index, name="Index"),
    path('Votesperregion/',views.Votesperregion, name="Votesperregion"),
    path('Responses/',views.Responses, name="Responses"),
    path('Mainpage/',views.Mainpage, name="Mainpage"),
    path('delete/<int:id>', views.delete, name='delete'),
    path('edit/<int:id>', views.edit, name='edit'),
    ]
