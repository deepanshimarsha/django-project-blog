from django.urls import path
from rest_framework.routers import SimpleRouter
from organizer import views
from .viewsets import TagViewSet

api_router = SimpleRouter()
api_router.register("tag", TagViewSet, basename="api-tag")
api_routes = api_router.urls

urlpatterns = api_routes + [

    path("startup/", views.StartupApiList.as_view(), name="api-startup-list"),
    path("startup/<str:slug>/", views.StartupApiDetail.as_view(), name="api-startup-detail"),
    path("newslink/", views.NewsLinkApiList.as_view(), name="api-newslink-list"),
    path("newslink/<str:startup_slug>/<str:newslink_slug>/", views.NewsLinkApiDetail.as_view(), name="api-newslink-detail"),
]