from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('create_post/', views.create_post, name='create_post'),
    path('tweet_post/', views.tweet_post, name='tweet_post'),
]
