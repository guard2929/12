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

]

