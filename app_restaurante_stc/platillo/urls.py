from django.urls import path
from . import views

urlpatterns = [
    path('platillo_list/', views.platillo_list, name='platillo_list'),
    path('platillo_details/', views.platillo_details, name='platillo_details'),
    path('platillo_create/', views.platillo_create, name='platillo_create'),
    path('platillo_delete15/', views.platillo_delete15, name='platillo_delete15'),

]