from django.urls import path
from .views import (
    PostDetail,
    PostList,
)

urlpatterns = [
    path("", PostList.as_view(), name="post-list"),
    path("<int:year>/<int:month>/<str:slug>/", PostDetail.as_view(), name="post-detail"),
]