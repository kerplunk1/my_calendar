from django.urls import path
from . import views


urlpatterns = [
    path('get_get_actions_in_year/<int:year>/', views.get_actions_in_year),
    path('create/', views.create_new_action),
    path('create/<str:action>/', views.create_new_action)
]

