from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('send-email/', views.send_email, name='send-email'),
]
