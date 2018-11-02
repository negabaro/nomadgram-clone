from rest_framework import serializers
from . import models
from nomadgram.users import models as user_models


class FeedUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = user_models.User
        fields = (
          'username',
          'profile_image'
        )
        
class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Comment
        #fields = '__all__'
        fields = (
          'id',
          'message',
          'creator'
        )


class LikeSerializer(serializers.ModelSerializer):

    #image = ImageSerializer()
    
    class Meta:
        model = models.Like
        fields = '__all__'



class ImageSerializer(serializers.ModelSerializer):

    #comment_set = CommentSerializer(many=True)
    #like_set = LikeSerializer(many=True)
    #after migrate
    comments = CommentSerializer(many=True)
    #likes = LikeSerializer(many=True)
    creator = FeedUserSerializer()
    
    class Meta:
        model = models.Image
        #fields = '__all__'
        fields = (
              'id',
              'file',
              'location',
              'caption',
              'comments',
              #'likes',
              'like_count',
              #property설정
              'creator'
            )


