from django.db import models
from nomadgram.users import models as user_models

# Create your models here.
class TimeStampedModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Image(TimeStampedModel):

    file = models.ImageField()
    location = models.CharField(max_length=140)
    caption = models.TextField()
    #creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE, null=True)
    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE, null=True, related_name='images') #for following_user.images.all()
    
    @property
    def like_count(self):
        return self.likes.all().count()
    #like숫자만 보고싶기에 프로퍼티를 작성
    
    
    def __str__(self):
        return self.location
    class Meta:
        ordering = ['-created_at']
        #db에서 얻은 리스트를 생성된 날짜로 정렬할 수 있게 
        #메타클래스는 이처럼 모델의 설정을 위해서 사용
        
class Comment(TimeStampedModel):

    message = models.TextField()
    creator = models.ForeignKey(user_models.User,on_delete=models.CASCADE, null=True)
    image = models.ForeignKey(Image,on_delete=models.CASCADE, null=True, related_name='comments')
    
    def __str__(self):
        return self.message
    
class Like(TimeStampedModel):
    creator = models.ForeignKey(user_models.User,on_delete=models.CASCADE, null=True)
    image = models.ForeignKey(Image,on_delete=models.CASCADE, null=True, related_name='likes')
    
    def __str__(self):
        return '{} - {}'.format(self.creator.username, self.image.caption)
    
 