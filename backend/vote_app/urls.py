from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('categories/', views.all_categories),
    path('categories/<slug:slug>/', views.category_detail),
    path('vote/', views.vote),
]
