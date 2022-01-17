from django.urls import path, include
from basic_algo import views

urlpatterns = [
	path('', views.index, name='index'),
]