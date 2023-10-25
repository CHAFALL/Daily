from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('new/', views.new, name = 'new'),
    path('create/', views.create, name='create'),
    # 삭제는 뭐를 삭제할 껀데를 알아야 해서 조회가 필요(수정도 동일)
    # <int:pk> 있어야 됨(조회는)(pk variable routing)
    path('<int:pk>/delete/',views.delete, name='delete'),
    # edit은 new를 참고하면 됨(전반적으로)
    path('<int:pk>/edit/', views.edit, name='edit'),
    # update는 create를 참고하면 됨(전반적으로)
    path('<int:pk>/update/', views.update, name='update'),
]
