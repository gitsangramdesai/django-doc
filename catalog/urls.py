from django.urls import path
from . import views

app_name = 'catalog'
urlpatterns =[
    path('products/',views.ProductList.as_view()),
    path('products/<int:pk>',views.ProductDetail.as_view()),
    path('products/<int:pk>/reviews/',views.ReviewList.as_view()),
    path('products/<int:product_id>/reviews/<int:review_id>/',views.ReviewDetail.as_view()),
]