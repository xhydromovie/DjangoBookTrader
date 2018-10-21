from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('advertisement/<int:id>/report/', views.report, name='report'),
    path('advertisement-create/', views.advertisement_creat, name='advertisement-creat'),
]
