from django.urls import path
from .import views

urlpatterns = [
    path('',views.IndexView.as_view(),name='home'),
    path('profile/',views.ProfileView.as_view(),name='profile'),
    path('message/',views.MessageView.as_view(),name='message'),
    path('notification/',views.NotificationView.as_view(),name='notification'),
    path('login/',views.LoginView.as_view(),name='login'),
    path('register/',views.RegisterView.as_view(),name='register'),
    path('like/<int:content_id>/', views.like, name="weblike"),
    path('stories/',views.StoriesView.as_view(), name='stories')

]