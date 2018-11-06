from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers
from rest_framework import status

class ExploreUsers(APIView):
    
    def get(self, request, format=None):
        
        #last_five = models.User.objects.all().order_by('-created_at')[:5]
        last_five = models.User.objects.all().order_by('-date_joined')[:5]
        #date_joined 최근가입순으로 정렬
         
        serializer = serializers.ExploreUserSerializer(last_five, many=True)
        
        return Response(data=serializer.data, status=status.HTTP_200_OK)
        
    
#http://192.168.0.17:8000/users/2/follow/ post시 2번유저 팔로우
class FollowUser(APIView):

    def post(self, request, user_id, format=None):

        user = request.user

        try:
            user_to_follow = models.User.objects.get(id=user_id)
        except models.User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        user.following.add(user_to_follow)

        user.save()

        return Response(status=status.HTTP_200_OK)

# http://192.168.0.17:8000/users/2/unfollow/ post시 2번유저 팔로우를 삭제

class UnFollowUser(APIView):

    def post(self, request, user_id, format=None):

        user = request.user

        try:
            user_to_follow = models.User.objects.get(id=user_id)
        except models.User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        user.following.remove(user_to_follow)

        user.save()

        return Response(status=status.HTTP_200_OK)

class UserProfile(APIView):

    def get(self, request, username, format=None):

        try:
            found_user = models.User.objects.get(username=username)
        except models.User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.UserProfileSerializer(found_user)

        return Response(data=serializer.data, status=status.HTTP_200_OK)