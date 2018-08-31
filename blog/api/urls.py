from django.urls import path
from blog.api import views

urlpatterns = [
    path('post/', views.PostListView.as_view()),
    path('post/<uuid:pk>/', views.PostView.as_view()),
]
