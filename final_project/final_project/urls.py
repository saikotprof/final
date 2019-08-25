from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_view
from users import views as user_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_view.register, name='register'),
    path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(), name='logout'),
    path('', include('blog.urls')),
]
