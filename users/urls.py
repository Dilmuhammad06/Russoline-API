from django.urls import path
from .import views

app_name='auth'

urlpatterns = [
    path('login/',views.LoginAPI.as_view()),
    path('logout/',views.LogoutAPI.as_view()),
    path('register/',views.RegisterAPI.as_view()),
]
