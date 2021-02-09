from django.urls import path
from .views import *



urlpatterns = [
    
    # path('product_list/',product_list),
    # path('product_detail/<int:pk>',product_detail),
    path('login_page/',login_page),
    path('control_panel/',control_panel),

    #api
    path('product_list/',ProductList.as_view()),
    path('product_detail/<int:id>',ProductDetails.as_view()),
    path('machine_list/',MachineList.as_view()),
    path('machine_detail/<int:id>',MachineDetails.as_view()),
    path('machine_add_product/<int:id>',MachineAddProduct.as_view()),
    path('transaction_list/',TransactionList.as_view()),
    path('transaction_detail/<int:id>',TransactionDetails.as_view()),
    path('restock_list/',RestockList.as_view()),
    path('restock_detail/<int:id>',RestockDetails.as_view()),
    path('login/',Login.as_view()),
    path('logout/',Logout.as_view()),

    #監控
    #操作
]
