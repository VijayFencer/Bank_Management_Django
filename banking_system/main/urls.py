# main/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login',views.login_view,name='login'), 
    path('dashboard',views.dashboard,name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('update_user',views.update_user,name='update'),
    path('create_transaction',views.create_transaction,name='transactions'),
    path('transaction_history',views.trans_hist,name='history'),
]
