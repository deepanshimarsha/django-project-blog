from django.urls import path
from .views import (
    TagDetail,
    TagList,
    StartupDetail,
    StartupList,

)

urlpatterns = [
    path("tag/", TagList.as_view(), name="tag-list"),
    path("tag/<str:slug>/", TagDetail.as_view(), name="tag-detail"),
    path("startup/",StartupList.as_view(), name="startup-list"),
    path("startup/<str:slug>/", StartupDetail.as_view(), name="startup-detail"),
]