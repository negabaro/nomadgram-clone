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