from django.contrib.auth import views as auth_view
from django.urls import path
from .import views


urlpatterns = [
    path('sign_up/', views.sign_up, name='users-sign-up'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='users-login')
]