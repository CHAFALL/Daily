from django.shortcuts import render

# Create your views here.
# 여기서 request는 약속이다.(없으면 views 동작 x)
def index(request):
    # 메인 페이지를 응답
    # html로 만들어서 준다.(반환)
    # 'articles/index.html': 템플릿 경로임
    return render(request, 'articles/index.html')
