from django.contrib import auth
from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',views.home_page,name='home_page'),
    path('register',views.registration_view,name='registration_view'),
    path('login',views.login_view,name='login'),
    path('logout',views.logout_view,name='logout'),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
