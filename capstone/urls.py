"""capstone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from webapp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('', include('webapp.urls')),
    path('blog/', include('blog.urls')),
    path('user_auth/', include('django.contrib.auth.urls')),
    path('user_auth/', include('user_auth.urls')),
    path('login/', include('login.urls'), name='login'),
    path('register/', include('register.urls')),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),


    
]
