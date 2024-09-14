from django.urls import path
from .forms import LoginForm
from .views import home, RegisterView, CustomLoginView, CustomLogout, ResetPasswordView, ChangePasswordView, dashboard
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='account/login.html',
                                           authentication_form=LoginForm), name='login'),
#     path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'), name='logout'),
    path('logout/', CustomLogout, name='logout'),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
    path('password-change/', ChangePasswordView.as_view(), name='password_change')
]