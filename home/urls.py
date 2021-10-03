

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('bookingpage', views.booked,name='booked'),
    path('cart', views.cart,name='cart'),
    path('contactus', views.contactus,name='contactus'),
    path('filter', views.filter,name='filter'),
    path('LocalStore', views.LocalStore,name='LocalStore'),
    path('product', views.product,name='product'),
    path('productssfe', views.productssfe,name='productssfe'),
    path('sports_acces', views.sports_acces,name='sports_acces'),
    path('sports_events', views.sports_events,name='sports_events'),
    path('sports_store', views.sports_store,name='sports_store'),
    path('TicketBooking', views.TicketBooking,name='TicketBooking'),

]