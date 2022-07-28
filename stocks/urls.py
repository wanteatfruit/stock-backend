from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('<str:table_name>/', views.query, name='query')
]