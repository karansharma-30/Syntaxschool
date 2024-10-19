
from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile', profile_view, name='profile'),
    path('profile/view/', views.profile_view, name='profile_view'),
    path('profile/remove_picture/', views.remove_profile_picture, name='remove_profile_picture'),
    path('forgot-password/',ForgotPassword,name='forgot-password'),
    path('password-reset-sent/<str:reset_id>/',passwordResetSent,name="password-reset-sent"),
    path('reset-password/<str:reset_id>/',ResetPassword,name="reset-password"),
    path('profile_redirect_view/', views.profile_redirect_view, name='profile_redirect'), 
    
]
