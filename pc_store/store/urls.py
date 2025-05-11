from django.urls import path
from django.contrib.auth import views as auth_views
from .views import index, register, configure_pc

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='store/login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('configure/', configure_pc, name='configure_pc'),
path('profile/', views.profile_view, name='profile'),
path('change-password/', views.change_password, name='change_password'),
path('delete-account/', views.delete_account, name='delete_account'),

]

from django.contrib.auth import views as auth_views

urlpatterns += [
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='store/password_reset.html',
             email_template_name='store/password_reset_email.html',
             subject_template_name='store/password_reset_subject.txt',
         ), name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='store/password_reset_done.html'
         ), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='store/password_reset_confirm.html'
         ), name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='store/password_reset_complete.html'
         ), name='password_reset_complete'),
]

