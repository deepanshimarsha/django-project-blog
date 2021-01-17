from django.urls import path
from organizer import views

urlpatterns = [
    path("tag/", views.TagApiList.as_view(), name="api-tag-list"),
    path("tag/<str:slug>/", views.TagApiDetail.as_view(), name="api-tag-detail"),
    path("startup/", views.StartupApiList.as_view(), name="api-startup-list"),
    path ("startup/<str:slug>/", views.StartupApiDetail.as_view(), name="api-startup-detail"),
]