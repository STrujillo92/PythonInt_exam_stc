from django.urls import path
from . import views

urlpatterns = [
    path('mesero_list/', views.mesero_list, name='mesero_list'),
    path('mesero_details/', views.mesero_details, name='mesero_details'),
    path('mesero_age_update/', views.mesero_age_update, name='mesero_age_update'),
    path('mesero25_list_serializer/', views.ListMeseroSerializer25,name='mesero25_list_ssr'),
    path('mesero_create_vbc',views.MeseroCreate.as_view(),name='mesero_create_vbc'),
    path('mesero_listp_vbc',views.MeseroListP.as_view(),name='mesero_listp_vbc'),
    path('mesero_edit_vbc/<int:pk>',views.MeseroUpdate.as_view(),name='mesero_edit_vbc'),
    path('mesero_delete_vbc/<int:pk>',views.MeseroDelete.as_view(),name='mesero_delete_vbc'),
    path('mesero_list_serializer/', views.ListMeseroSerializer, name='mesero_list_ssr'),
    path('mesero_list_drf_def/',views.mesero_api_view,name='mesero_list_drf'),
    path('mesero_detail_drf_def/<int:pk>', views.mesero_details_view, name='mesero_detail_drf'),

]