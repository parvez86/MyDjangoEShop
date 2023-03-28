from django.urls import path
from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name="store"),
	path('login/', views.login_request, name="login"),
	path('logout/', views.logout_request, name="logout"),
	path('register/', views.register_request, name="register"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('product/<int:id>', views.single_product, name="single_product"),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
]