from django.urls import path
from .views import AllUserView, currentUserView, getAnyUser

urlpatterns = [
    path("all-users/", AllUserView.as_view(), name="Home"),
    path("current-user/", currentUserView.as_view(), name="current-user"),
    path("get-user/<str:pk>/", getAnyUser.as_view(), name="any-user"),
]
