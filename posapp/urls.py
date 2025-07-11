from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('sale/', views.sale_form, name='sale_form'),
    path('report/', views.sales_report, name='sales_report'),  
    path('login/', auth_views.LoginView.as_view(template_name='posapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

]