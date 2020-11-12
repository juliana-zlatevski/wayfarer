from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('accounts/signup', views.signup, name='signup'),
    path('profile/new/', views.new_profile, name='new_profile'),
    path('profile/<int:profile_id>/', views.user_profile, name='user_profile'),
    path('profile/<int:profile_id>/edit/', views.edit_profile, name='edit_profile'),
    path('cities/', views.cities, name='cities'),
    path('post/<int:post_id>/', views.view_post, name='view_post'),
    path('city/<int:city_id>/', views.view_city, name='view_city'),
    path('city/<int:city_id>/add_post/', views.add_post, name='add_post'),
    path('city/<int:city_id>/remove_post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('post/<int:post_id>/edit/', views.edit_post, name='edit_post'),
]