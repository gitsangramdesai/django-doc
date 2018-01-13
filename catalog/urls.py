from django.urls import path
from . import views

app_name = 'catalog'
urlpatterns =[
    path('products/', views.ProductList.as_view()),
    path('products/<int:pk>', views.ProductDetail.as_view()),
]