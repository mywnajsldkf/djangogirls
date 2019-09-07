# from, import : 다른 파일에 있는 것을 추가함
from django.db import models
from django.utils import timezone

# 모델(객체, object)을 정의함
# class Post(models.Model): 
class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    # CharField - 글자 수가 제한된 텍스트를 정의함, 짧은 문자열 정보를 저장
    title = models.CharField(max_length=200)
    # TextField - 글자 수에 제한이 없는 긴 텍스트를 위한 속성
    text = models.TextField()
    # DateTimeField - 날짜와 시간을 의미
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title