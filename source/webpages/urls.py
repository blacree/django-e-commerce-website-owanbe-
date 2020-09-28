from django.urls import path
app_name = 'webpages'
from . import views

urlpatterns = [

    path('', views.home, name='homepage'),
    path('tech/', views.tech, name='techpage'),
    path('feedback/', views.feedback, name='feedback'),
]

