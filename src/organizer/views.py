from .models import Tag, Startup, NewsLink
from .serializers import TagSerializer, StartupSerializer, NewsLinkSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView

class TagList(ListView):
    queryset = Tag.ojects.all()
    template_name = "tag/list.html"

class TagDetail(DetailView):
    queryset = Tag.objects.all()
    template_name = "tag/detail.html"


class TagApiDetail(RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = "slug"

class TagApiList(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class StartupApiDetail(RetrieveAPIView):
    queryset = Startup.objects.all()
    serializer_class = StartupSerializer
    lookup_field = "slug"

class StartupApiList(ListAPIView):
    queryset = Startup.objects.all()
    serializer_class = StartupSerializer

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



