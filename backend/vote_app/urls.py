from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.all_categories),
    path('categories/<slug:slug>/', views.category_detail),
    path('vote/', views.vote),
]
