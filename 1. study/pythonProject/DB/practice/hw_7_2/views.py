from .serializers import __(a)__
from rest_framework.response import __(d)__
from .serializers import Article
from rest_framework.decorators import api_view

@api_view(['GET'])
def article_list(request):
    articles = Article.objects.all()
    serializer = __(a)__(articles, __(c)__)
    return __(d)__(serializer.__(e)__)


# (a) : ArticleSerializer
# (c) : many=True
# (d) : Response
# (e) : data
