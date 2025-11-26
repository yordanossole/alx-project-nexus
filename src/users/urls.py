from django.urls import path
from .views import MyProfileView, UserProfileView, FollowUserView, UnFollowUserView

urlpatterns = [
    # path("user-login/", )
    path("me/", MyProfileView.as_view(), name="my-profile"),
    # path("<str:username>/") # view own profile
    path("<str:username>/", UserProfileView.as_view(), name="user-profile"),
    path("<str:username>/follow/", FollowUserView.as_view(), name="user_to_follow"), # follow user
    path("<str:username>/unfollow/", UnFollowUserView.as_view(), name="user_to_unfollow"), # unfollow user

]
