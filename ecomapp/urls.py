from django.urls import path
from . import views




urlpatterns=[ 
    path('login/', views.login_user, name='login'),
    path('home/', views.home, name='home'),
    
    path('register/', views.register, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('',views.home),
    path('Product/', views.product_list, name='product_list'),            # Read
    path('Product/<int:id>/', views.product_detail, name='product_detail'),  # Detail view
    path('Product/create/', views.product_create, name='product_create'),    # Create
    path('Product/<int:id>/update/', views.product_update, name='product_update'),  # Update
    path('Product/<int:id>/delete/', views.product_delete, name='product_delete'),  # delete

]

