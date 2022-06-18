from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^(?P<hash>[\w-]+)/', views.redirect, name='redirect')
]
