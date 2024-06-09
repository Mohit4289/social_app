from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', UserDetailView.as_view(), name='profile'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('search/', UserSearchView.as_view(), name='user-search'),
    path('friend/request/', SendFriendRequestView.as_view(), name='send-friend-request'),
    path('friend/accept/', AcceptFriendRequestView.as_view(), name='accept-friend-request'),
    path('friend/reject/', RejectFriendRequestView.as_view(), name='reject-friend-request'),
    path('friend/list/', FriendListView.as_view(), name='friend-list'),
    path('friend/requests/pending/', PendingFriendRequestsView.as_view(), name='pending-friend-requests'),


]
