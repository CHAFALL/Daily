from rest_framework import serializers
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)


class CommentSerializer(serializers.ModelSerializer):
    # title필드만 변환해주는 serializer가 기존에 없어서 이 안쪽에서 새로 정의할 것임(밖에 있었다면 밖에 것을 가져다 쓰면 됨), (이 클래스는 이 안에서만 씀, 그래서 이름도 같아도 되네?? 밖의 것들이랑)
    class ArticleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('title',)
    # override
    article = ArticleSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        # override를 하는 순간 아래의 코드는 먹히지 않게 됨(주석처리)(대신에 위(override 부분)에서 처리)
        # 아래의 것은 아무런 손도 대지 않은 기본 필드만 가능
        # read_only_fields = ('article',)


class ArticleSerializer(serializers.ModelSerializer):
    # 이건 원래 존재했다. 매니저로써, 다만 정의를 해주지 않으면 기본적으로 출력 x
    # 1-> N을 조회할려고 하므로 many=True
    # 그리고 이걸 읽기 전용 필드로 바꾸지 않으면 오류 발생
    # 왜냐하면 지금 이 필드를 활성화 시켰기 때문에, 검사 진행함..
    # 참고: 이렇게 하면 불필요해 보이는 것도 많이 출력되는데 이것도 override로 바꿀 수 있음
    # 역참조 이름이랑 정확히 같아야 됨(comment_set)
    comment_set = CommentSerializer(many=True,read_only=True)
    # 전에 배운데서는 article.comment_set.count()이런식으로 씀
    # 이걸 활용할 것인데 ArticleSerializer클래스는 article을 기반으로 만들어진 것이라서 앞의 인스턴스 제외.
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'



