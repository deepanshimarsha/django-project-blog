from .models import Post
from .serializers import PostSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from django.views import View

class PostList(ListView):
    model = Post
    template_name = "post/list.html"

class PostDetail(View):
    def get(self, request, year, month, slug):
        post = get_object_or_404(
            Post,
            pub_date__year=year,
            pub_date__month=month,
            slug=slug,

        )
        context = {"post": post}
        return render(request, "post/detail.html", context)



