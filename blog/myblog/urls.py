from django.contrib import admin
from django.urls import path, include
from .views import HomeView, ArtDetView, PushView, UpPostView, DelView

urlpatterns = [
    path('',HomeView.as_view(),name="home"),
    path("admin/", admin.site.urls, name="login"),
    path('article/<int:pk>',ArtDetView.as_view(), name="article-detail"),
    path('push/',PushView.as_view(), name="push"),
    path('article/edit/<int:pk>',UpPostView.as_view(), name="update"),
    path('article/edit/<int:pk>/remove',DelView.as_view(), name="delete"),
]