from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('top-sellers', topSellers, name='top-sellers'),
    path('advertisement-post', advertisementPost, name='advertisement-post'),
    path('register', register, name='register'),
    path('login', login, name='login'),
    path('profile', profile, name='profile'),
    path('advertisement', advertisement, name='advertisement')
]
