from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('image-selection/', views.image_page, name='image-selection'),
    path('details/<int:id>/', views.details, name='details'),
    path('search/', views.search, name='search'),
    path('about/', views.about, name='about'),
    path('add/', views.add_image, name='add'),
    path('contact/', views.contact, name='contact'),
]