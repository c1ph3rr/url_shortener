from urllib import request
from django.urls import path

from . import views

urlpatterns = [
    path('', views.CreateUrl.as_view()),
    path('<hash>', views.RedirectUrl.as_view())
]
