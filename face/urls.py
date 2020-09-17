from django.urls import path
from face import views

urlpatterns = [
    path('', views.indexView, name="home"),
    path('prediction', views.predictionView, name="prediction"),
    path('result', views.resultView, name="result"),
]
