from .serializers import __(a)__
from rest_framework.response import __(d)__
from .serializers import Article
from rest_framework.decorators import api_view

@api_view(['GET'])
def article_list(request):
    articles = Article.objects.all()
    serializer = __(a)__(articles, __(c)__)
    return __(d)__(serializer.__(e)__)


# 여기서 serializer는 객체이다 그러므로 객체를 보낼 수는 없으므로 serializer.data를 보냄

# (a) : ArticleSerializer
# (c) : many=True
# (d) : Response
# (e) : data
