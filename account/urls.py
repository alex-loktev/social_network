from django.urls import path
from django.contrib.auth import views as auth_view
from .views import *


urlpatterns = [
    path('login/', auth_view.LoginView.as_view(), name='login'),
    path('logout/', auth_view.LogoutView.as_view(), name='logout'),
    path('password_change/', auth_view.PasswordChangeView.as_view(), name='password_change'),
    path('password_change_done/', auth_view.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password-reset/', auth_view.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_view.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_view.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_view.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('registration/', RegistrationView.as_view(), name='RegistrationView'),
    path('dashboard/', dashboard, name='dashboard'),
    path('edit/', EditProfileView.as_view(), name='EditProfileView')
]