from django.urls import path
from . import views

from django.contrib.auth.views import LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView

urlpatterns = [
    path('sign_up/', views.sign_up, name="sign_up"),
    path('login/', views.ViewLogIn.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page='login'), name="logout"),

    path("password-reset/", PasswordResetView.as_view(template_name='accounts/reset/password_reset.html'),
         name="password_reset"),
    path("password-reset/done/", PasswordResetDoneView.as_view(template_name='accounts/reset/password_reset_done.html'),
         name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>/",
         PasswordResetConfirmView.as_view(template_name='accounts/reset/password_reset_confirm.html'),
         name="password_reset_confirm"),
    path("password-reset-complete/",
         PasswordResetCompleteView.as_view(template_name='accounts/reset/password_reset_complete.html'),
         name="password_reset_complete"),
    path('resendOTP', views.resend_otp),
]
