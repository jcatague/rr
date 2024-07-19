from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('reservation/', views.reservation, name='reservation'),
    path('choose_table/<int:reservation_id>/', views.choose_table, name='choose_table'),
    path('save_reservation/', views.save_reservation, name='save_reservation'),
    path('get_reservation/', views.get_reservation, name='get_reservation'),
    path('myreserve/', views.my_reserve_view, name='myreserve'),
    path('api/confirm/', views.confirm_reservation, name='confirm_reservation'),
    path('api/tables/', views.get_tables, name='get_tables'),
]
