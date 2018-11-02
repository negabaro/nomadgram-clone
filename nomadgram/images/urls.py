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
