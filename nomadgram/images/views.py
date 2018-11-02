from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers

# Create your views here.
class ListAllImages(APIView):

    def get(self, request, format=None):

        all_images = models.Image.objects.all()

        serializer = serializers.ImageSerializer(all_images, many=True)

        return Response(data=serializer.data)
        
class ListAllComments(APIView):

     def get(self, request, format=None):

         #all_comments = models.Comment.objects.all()
         #all_comments = models.Comment.objects.filter(id=2)
         user_id = request.user.id
         all_comments = models.Comment.objects.filter(creator=user_id)
         serializer = serializers.CommentSerializer(all_comments, many=True)

         return Response(data=serializer.data)


class ListAllLikes(APIView):

     def get(self, request, format=None):

         all_likes = models.Like.objects.all()

         serializer = serializers.LikeSerializer(all_likes, many=True)

         return Response(data=serializer.data)

class Feed(APIView):
     def get(self, request, format=None):
         
         user = request.user
         following_users = user.following.all()
         image_list = []
         
         #print(following_users)
         for following_user in following_users:
             #print(following_user.images.all())
             user_images = following_user.images.all()[:2]
             #2개의 이미지만 받고싶을떄 
             
             #팔로잉 하고 있는 복수유저의 이미지를 가져와서 
             
             for image in user_images:
                 
                 image_list.append(image)
                 #이미지 리스트에 저장
        
         print(image_list)
         #sorted_list = sorted(image_list, key=get_key)
         #sorted_list = sorted(image_list, key=get_key, reverse=True)
         
         sorted_list = sorted( image_list, key=lambda image: image.created_at, reverse=True)
         
         #정렬시켜 주기
        
         print(sorted_list)
        
        
         serializer = serializers.ImageSerializer(sorted_list, many=True)
             
         
         #return Response(status=200)
         #일단 에러 회피를 위해
         
         return Response(serializer.data)
         
         #http://192.168.0.17:8000/images/feed/
         #success!!
         
     #def get_key(image):
     #    return image.created_at
     #lambda로 정의했기에 없어도됨