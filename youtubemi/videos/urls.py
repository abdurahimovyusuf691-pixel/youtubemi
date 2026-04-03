from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'videos'

urlpatterns = [
    path('', views.video_list, name='video_list'),
    path('<int:pk>/', views.video_detail, name='video_detail'),
    path('create/', views.video_create, name='video_create'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='videos:video_list'), name='logout'),
    path('signup/', views.signup_view, name='signup'),  
    path('accounts/profile/', views.profile_view, name='profile'),
    path('like/<int:pk>/', views.like_video, name='like_video'),
    path('dislike/<int:pk>/', views.dislike_video, name='dislike_video'),
    path('subscribe/<int:video_id>/', views.toggle_subscribe, name='toggle_subscribe'),
    path('<int:pk>/comment/', views.add_comment, name='add_comment'),
    path('podpiski/', views.subscribed_videos, name='subscribed_videos'),
    path('subscribe-author/<int:author_id>/', views.toggle_subscribe, name='toggle_subscribe'),
    path('author/<int:author_id>/', views.author_videos, name='author_videos'),

]

