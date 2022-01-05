from django.urls import path
from . views import ProductList,CreateProduct,DetailViewProduct,ProductUpdate,DeleteView

urlpatterns = [
    path('product/',ProductList.as_view(),name='product-list'),
    path('create_product/',CreateProduct.as_view(),name='create_product'),
    path('product_detail/<int:pk>/',DetailViewProduct.as_view(),name='product_detail'),
    path('product_update/<int:pk>/',ProductUpdate.as_view(),name='product_update'),
    path('product_delete/<int:pk>/',DeleteView.as_view(),name='product_delete'),  
]
