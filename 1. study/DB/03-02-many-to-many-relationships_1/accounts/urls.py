from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('profile/<str:username>/', views.profile, 
    name='profile'),
    # 아래와 같이 하면 문제가 발생할 수 있다.(문자로 들어오는 모든 것들을 username으로 보겠다는 것이므로)
    # path('<username>/', views.profile, name='profile')
    path('<int:user_pk>/follow/', views.follow, name='follow'),
]
