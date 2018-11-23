from rest_framework import serializers
from . import models
from nomadgram.users import models as user_models
from taggit_serializer.serializers import (TagListSerializerField,
                                            TaggitSerializer)
from . import models
class SmallImageSerializer(serializers.ModelSerializer):

    """ Used for the notifications """

    class Meta:
        model = models.Image
        fields = (
            'file',
        )

class FeedUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = user_models.User
        fields = (
          'username',
          'profile_image'
        )
        
class CommentSerializer(serializers.ModelSerializer):
    creator = FeedUserSerializer(read_only=True)
    #creator같은경우 유저가 직접입력하는게 의미가없으므로 read_only=True옵션을 지정해주면 inValid되게됨
    
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



class ImageSerializer(TaggitSerializer, serializers.ModelSerializer):

    #comment_set = CommentSerializer(many=True)
    #like_set = LikeSerializer(many=True)
    #after migrate
    comments = CommentSerializer(many=True)
    #likes = LikeSerializer(many=True)
    creator = FeedUserSerializer()
    tags = TagListSerializerField()
    
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
              'creator',
              'tags',
              'created_at'
            )

class UserProfileImageSerializer(serializers.ModelSerializer):

     class Meta:
         model = models.Image
         fields = (
             'id',
             'file',
             'comment_count',
             'like_count'
         )



class InputImageSerializer(serializers.ModelSerializer):

     class Meta:
         model = models.Image
         fields = (
             'file',
             'location',
             'caption',
         )