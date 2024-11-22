from django.urls import path

from blog.urls import urlpatterns
from .views import PostList, PostDetail


app_name= "blog_api"

urlpatterns = [
    path('<int:pk>/', PostDetail.as_view(), name='detailcreate'),#detail view of the post
    path('', PostList.as_view(), name='listcreate'), #showing one of the post
]
