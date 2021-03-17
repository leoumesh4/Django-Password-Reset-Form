from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.homePage, name="home"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutPage, name="logout"),
    path('reset-password/', auth_views.PasswordResetView.as_view(template_name="demo/reset-password.html"), name="reset_password"),
    path('reset-link-sent/', auth_views.PasswordResetDoneView.as_view(template_name="demo/reset-sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="demo/reset-form.html"), name="password_reset_confirm"),
    path('reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name="demo/reset-done.html"), name="password_reset_complete"),
]