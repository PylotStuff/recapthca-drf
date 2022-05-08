from django.urls import path

from account.api import views

urlpatterns = [
    path('register/',
         views.RegisterUserAPIView.as_view(), name='register'),
]