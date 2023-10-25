from .serializers import ArticleSerializer
from rest_framework.response import Response
from .model import import article


@api_view(['GET'])
def Article_list(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, __(d)__)
    return __(e)__(serializer.data)

# (d) : many=True
# (e) : Response