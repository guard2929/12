from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('about/', views.about, name='about'),
    path('faq/', views.faq, name='faq'),
    path('contacts/', views.contacts, name='contacts'),
    path('privacy/', views.privacy_policy, name='privacy_policy'),
    path('login/', auth_views.LoginView.as_view(template_name='store/login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('configure/', views.configure_pc, name='configure_pc'),
    path('accounts/profile/', views.profile, name='profile'),
    path('change-password/', views.change_password, name='change_password'),
    path('delete-account/', views.delete_account, name='delete_account'),
    path('order/<int:build_id>/', views.order_pc_build, name='order_pc_build'),
    path('build/delete/<int:build_id>/', views.delete_build, name='delete_build'),
    path('order_prebuilt/<int:product_id>/', views.order_prebuilt, name='order_prebuilt'),
]

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

