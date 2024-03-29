from django.urls import path
from .import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='blog-home'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
]
