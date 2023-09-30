from django.urls import path
from . import views


urlpatterns =[
    path('get-all-products/', views.get_all_products),
    path('get-subcategories-by-category/<int:pk>/', views.get_subcategories_by_category),
    path('get-product-by-subcategory/<int:pk>/', views.get_product_by_subcategory),
    path('filter-products-by-name/', views.filter_products_by_name),
    path('search-brand-by-name/', views.search_brand_by_name),
    path('get-products-by-sale/', views.get_products_by_sale),
    path('add-product-card/<int:pk>/', views.add_product_card),
    path('add-saved-product/<int:pk>/', views.add_saved_product),
    path('create_comment/<int:pk>/', views.create_comment),
    path('update-products-like/<int:pk>/', views.update_products_like)
]