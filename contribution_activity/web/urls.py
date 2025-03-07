from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:year>/', views.index, name='index'),
    path('create/', views.create_new_action),
    path('create/<str:action>/', views.create_new_action),
]

