from django.urls import path
from .import views

urlpatterns = [
    path('',views.IndexAPI().as_view(), name='home'),
    path('profile/',views.ProfileView.as_view(), name='profile'),
    path('upload/',views.UploadContentAPI.as_view()),
    path('content/<int:id>/',views.SingleContentAPI.as_view()),
    path("comment/",views.CommentAPI.as_view(), name='add_comment'),
    path("comment/<int:id>/",views.CommentEditAPI.as_view(), name='edit_comment'),
    path('action/like/<int:content>/',views.like, name='like'),
    path('action/follow/<int:creator>/',views.like, name='follow')
]
