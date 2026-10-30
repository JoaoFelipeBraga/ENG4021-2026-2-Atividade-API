"""
URL configuration for site_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.urls import path
from site_app import views

urlpatterns = [
    path("", views.movie_list, name="movie_list"),
    path('admin/', admin.site.urls),
    path('movies', views.create_movie),
    path('movies/update/<int:id>/', views.update_movie, name='update_movie'),
    path('movies/delete/<int:id>/', views.delete_movie, name='delete_movie')
] 

