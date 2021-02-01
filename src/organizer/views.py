from .models import Tag, Startup, NewsLink
from .serializers import TagSerializer, StartupSerializer, NewsLinkSerializer
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView


class TagList(ListView):
    queryset = Tag.objects.all()
    template_name = "tag/list.html"

class TagDetail(DetailView):
    queryset = Tag.objects.all()
    template_name = "tag/detail.html"

class StartupList(ListView):
    queryset = Startup.objects.all()
    template_name = "startup/list.html"

class StartupDetail(DetailView):
    queryset = Startup.objects.all()
    template_name = "startup/detail.html"


class NewsLinkApiDetail(RetrieveAPIView):
    queryset = NewsLink.objects.all()
    serializer_class = NewsLinkSerializer

    def get_object(self):
        startup_slug = self.kwargs.get("startup_slug")
        newslink_slug = self.kwargs.get("newslink_slug")

        queryset = self.filter_queryset(self.get_queryset())
        newslink = get_object_or_404(
            queryset,
            slug=newslink_slug,
            startup__slug=startup_slug,
        )
        self.check_object_permissions(
            self.request, newslink
        )
        return newslink

class NewsLinkApiList(ListAPIView):
    queryset = NewsLink.objects.all()
    serializer_class = NewsLinkSerializer



