from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('set/<int:pk>/', views.set_detail, name='set_detail'),
    path('artists/', views.participants_list, name='participants_list'),
    path('artist/<int:pk>/', views.participant_detail, name='participant_detail'),
    path('search/', views.search, name='search'),
]