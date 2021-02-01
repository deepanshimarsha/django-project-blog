from django.urls import path
from rest_framework.routers import SimpleRouter
from organizer import views
from .viewsets import TagViewSet, StartupViewSet



api_router = SimpleRouter()
api_router.register("tag", TagViewSet, base_name="api-tag")
api_router.register("startup", StartupViewSet, base_name="api-startup")
api_routes = api_router.urls

urlpatterns = api_routes + [

    path("newslink/", views.NewsLinkApiList.as_view(), name="api-newslink-list"),
    path("newslink/<str:startup_slug>/<str:newslink_slug>/", views.NewsLinkApiDetail.as_view(), name="api-newslink-detail"),
]