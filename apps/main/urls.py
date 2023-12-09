from django.urls import path
from . import views

urlpatterns = [
    # MAIN
    path('', views.main_view, name='main'),
    path('about/', views.about_view, name='about'),
    # BEAUTY
    path('beauty/', views.beauty, name='beauty'),
    path('beauty/<int:pk>/', views.BeautyDetail.as_view(), name='beauty_detail'),
    # Entertainment
    path('entertainment/', views.entertainment, name='entertainment'),
    path('entertainment/<int:pk>/', views.EntertainmentDetail.as_view(), name='entertainment_detail'),
    # PERSONALITEMS
    path('personalitems/', views.personalitems, name='personalitems'),
    path('personalitems/<int:pk>/', views.PersonalitemsDetail.as_view(), name='personalitems_detail'),
    # RESTAURANTS
    path('restaurants/', views.restaurants, name='restaurants'),
    path('restaurants/<int:pk>/', views.RestaurantsDetail.as_view(), name='restaurants_detail'),
    # TRANSPORT
    path('transport/', views.transport, name='transport'),
    path('transport/<int:pk>/', views.TransportDetail.as_view(), name='transport_detail'),
    # REALESTATE
    path('realestate/', views.realestate, name='realestate'),
    path('realestate/<int:pk>/', views.RealestateDetail.as_view(), name='realestate_detail'),

]
