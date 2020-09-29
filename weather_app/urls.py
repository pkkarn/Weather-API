from weather_app import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="index"),
    path('specific/', views.specific, name="specific"),

]
