from rest_framework.serializers import ModelSerializer
from .models import Post
from organizer.serializers import StartupSerializer, TagSerializer

class PostSerializer(ModelSerializer):

    startup = StartupSerializer(many=True)
    tags = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = "__all__"