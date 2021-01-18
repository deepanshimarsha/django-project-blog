from django.urls import path
from blog import views

urlpatterns = [
    path("post/", views.PostApiList.as_view(), name="api-blog-list"),
    path("post/<int:year>/<int:month>/<str:slug>/", views.PostApiDetail.as_view(), name="api-blog-detail"),
]