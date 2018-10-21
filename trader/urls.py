from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('advertisement-create/', views.advertisement_creat, name='advertisement-creat'),
    path('advertisement/<int:id>/report', views.report, name='report'),
    path('advertisement/<int:adv_id>', views.advertisement, name='advertisement')
]
