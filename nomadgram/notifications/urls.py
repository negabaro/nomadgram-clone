#from django.urls import path
from django.conf.urls import url
from . import views

app_name = "images"
urlpatterns = [
    url(
         regex=r'^$',
         view=views.Notifications.as_view(),
         name="notifications"  
    )
  
]