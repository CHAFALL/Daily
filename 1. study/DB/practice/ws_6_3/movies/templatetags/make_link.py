from django import template

register = template.Library()

@register.filter 
def hashtag_link(movie):
    # 여러개가 들어있을 수 있어서 ' '을 넣어줌
    content = movie.content + ' '
    hashtags = movie.hashtags.all()
    for hashtag in hashtags:
        # 비파괴함수라서 리턴 받아줘야됨
        content = content.replace(hashtag.content + ' ', f'<a href="/movies/{hashtag.pk}/hashtag/">{hashtag.content}</a> ') 
        # 위에도 한 칸 띄우는 디테일 필요
    return content