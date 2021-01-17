from rest_framework.serializers import HyperlinkedIdentityField, ModelSerializer
from .models import NewsLink, Tag, Startup

class TagSerializer(ModelSerializer):

    url = HyperlinkedIdentityField(view_name="api-tag-detail",)

    class Meta:
        model = Tag
        fields = "__all__"

class StartupSerializer(ModelSerializer):

    tags = TagSerializer(many=True)

    class Meta:
        model = Startup
        fields = "__all__"

class NewsLinkSerializer(ModelSerializer):

    startup = StartupSerializer()

    class Meta:
        model = NewsLink
        fields = "__all__"

