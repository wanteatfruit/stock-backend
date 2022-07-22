from django.urls import path

from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
# ]
urlpatterns = [
    # ex: /stocks/
    # path('', views.test, name='test'),
    # ex: /stocks/stocks_a
    path('<str:table_name>/', views.query, name='query'),
]