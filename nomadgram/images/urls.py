#from django.urls import path
from django.conf.urls import url
from . import views

app_name = "images"
urlpatterns = [
    url(
         regex=r'^$',
         view=views.Feed.as_view(),
         name="feed"  
    ),
    url(
         regex=r'(?P<image_id>[0-9]+)/like/',
         #위설정으로 url의 특정부분을 조작가능하게 된것!
         view=views.LikeImage.as_view(),
         name='like_image'
     ),
    url(
         regex=r'(?P<image_id>[0-9]+)/unlike/',
         #위설정으로 url의 특정부분을 조작가능하게 된것!
         view=views.UnLikeImage.as_view(),
         name='like_image'
     ),
     url(
         regex=r'(?P<image_id>[0-9]+)/comments/$',
         #$적는거 깜빡해서 밑에 ModerateComments가 루팅이 안되어서 삽질함..
         view=views.CommentOnImage.as_view(),
         name='comment_image'
     ),
     url(
         regex=r'^(?P<image_id>[0-9]+)/comments/(?P<comment_id>[0-9]+)/$',
         view=views.ModerateComments.as_view(),
         name='comment_image'
     ),
     url(
         regex=r'comments/(?P<comment_id>[0-9]+)/$',
         view=views.Comment.as_view(),
         name='comment'
     ),
     url(
         regex=r'search/$',
         view=views.Search.as_view(),
         name='search'
     ),    
  
]
#url사용할때는 regex필수였다
    

#app_name = "images"
#urlpatterns = [
#    path("all/", view=views.ListAllImages.as_view(), name="all_imaes"),
#    path("comments/", view=views.ListAllComments.as_view(), name="all_comments"),
#    path("likes/", view=views.ListAllLikes.as_view(), name="all_likes"),
#    path("feed/",view=views.Feed.as_view(), name="feed"),
#]
#연습용이었으므로 삭제 
