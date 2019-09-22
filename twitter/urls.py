from django.urls import path
from twitter.views import HomeView, LoginView, logout_view, MessagesView, AccountView, TweetInfoView, RegisterView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('messages/', MessagesView.as_view(), name='messages'),
    path('account/', AccountView.as_view(), name='account'),
    path('tweet/<int:tweet_id>', TweetInfoView.as_view(), name='tweet_info'),
]
