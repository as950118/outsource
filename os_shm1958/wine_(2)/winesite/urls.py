from django.conf.urls import url 
from . import views
from django.urls import path

urlpatterns = [
    path('index',views.index,name = 'index'),
    path('',views.index, name = 'index'),
    path('predict', views.predict, name = 'predict'),
]
