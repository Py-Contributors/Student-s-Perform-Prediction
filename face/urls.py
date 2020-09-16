from django.urls import path
from face.views import indexview

urlpatterns = [
    path('', indexview, name="home"),
]
