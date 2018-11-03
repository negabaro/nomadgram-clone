from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers
from rest_framework import status
#status안에 HTTP_404_NOT_FOUND,HTTP_201_CREATED를 사용하기위해

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

class LikeImage(APIView):

     def get(self, request, image_id, format=None):
     #def post(self, request, image_id, format=None):
     #원래는 post하는게 맞는데 body에 뭘 넘기고 하는건 아니고 테스트하기 쉬우므로 get을 이용
     
         user = request.user
     
         #http://192.168.0.17:8000/images/18/like/
         #에 억세스하면 print에 18이라는게 뜸
         print(image_id)
         
         
         try:
             
             found_image = models.Image.objects.get(id=image_id)
             #get대신에 fileter혹은 all이 될 수 도있음
         except models.Image.DoesNotExist:
             return Response(status=status.HTTP_404_NOT_FOUND)
        
         try:
             #http://192.168.0.17:8000/images/2/like/
             #해당 모델에 라이크가 있으면 그 라이크를 삭제하고
             preexsiting_like = models.Like.objects.get(
                 creator=user,
                 image=found_image
             )
             preexsiting_like.delete()
             
             return Response(status=status.HTTP_204_NO_CONTENT)
        
         except models.Like.DoesNotExist:
             #http://192.168.0.17:8000/images/2/like/
             #해당 모델의 라이크가 없으면 생성한다.
             new_like = models.Like.objects.create(
                 creator=request.user,
                 image=found_image
             )
         
             new_like.save()
             #http://192.168.0.17:8000/images/2/like/ 에 들어가면 현재유저이름으로 좋아요 1건이 추가됨
             #http://192.168.0.17:8000/admin/images/like/ 을 새로고침하면 추가되는걸 확인가능

             return Response(status=status.HTTP_201_CREATED)