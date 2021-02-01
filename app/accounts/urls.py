from django.urls import path

from django.contrib.auth.views import LogoutView
from . import views


app_name = 'accounts'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('tutorial/', views.TutorialLoginView.as_view(), name='tutorial'),
    path('profile/<int:pk>/', views.ProfileUpdateView.as_view(), name='profile'),
    path('follow/<int:following>/<int:followed>/', views.FollowView.as_view(), name='follow'),
]
