from django.urls import path, include

from shop import views

urlpatterns = [
    path('products/', views.ProductListView.as_view()),
    path('products/<int:product_id>/', views.download_product)
]