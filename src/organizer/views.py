

from django.shortcuts import get_object_or_404, get_list_or_404

from .models import Tag
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TagSerializer

class TagApiDetail(APIView):

    def get(self, request, pk):
        tag = get_object_or_404(Tag, pk=pk)
        s_tag = TagSerializer(
            tag,
            context={"request": request},
        )
        return Response(s_tag.data)

class TagApiList(APIView):

    def get(self, request):
        tag_list = get_list_or_404(Tag)
        s_tag = TagSerializer(
            tag_list,
            many=True,
            context={"request": request},
        )
        return Response(s_tag.data)

# Create your views here.
