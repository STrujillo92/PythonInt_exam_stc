from django.urls import path
from . import views

urlpatterns = [
    path('mesero_list/', views.mesero_list, name='mesero_list'),
    path('mesero_details/', views.mesero_details, name='mesero_details'),
    path('mesero_age_update/', views.mesero_age_update, name='mesero_age_update'),
]