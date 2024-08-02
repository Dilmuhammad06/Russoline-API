from django.urls import path
from .import views

urlpatterns = [
    path('',views.IndexView.as_view(),name='home'),
    path('profile/',views.ProfileView.as_view(),name='profile'),
    path('message/',views.MessageView.as_view(),name='message'),
    path('notification/',views.NotificationView.as_view(),name='notification'),
    path('explore/',views.ExploreView.as_view(),name='explore'),
    path('login/',views.LoginView.as_view(),name='login'),
    path('register/',views.RegisterView.as_view(),name='register'),
    
]