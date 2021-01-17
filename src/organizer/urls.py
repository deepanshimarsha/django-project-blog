from django.urls import path
from organizer import views

urlpatterns = [
    path("", views.TagApiList.as_view(), name = "api-tag-list"),
    path("<str:slug>/", views.TagApiDetail.as_view(), name="api-tag-detail")
]