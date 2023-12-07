from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()
# Create your models here.
class Post(models.Model):
    image = models.ImageField(verbose_name='이미지',null=True,blank=True)
    title = models.CharField(verbose_name='상품명',max_length=20,null=True,blank=True)
    sales = models.IntegerField(verbose_name='가격',default=0,null=True,blank=True)
    number = models.IntegerField(verbose_name='수량',default=0,null=True,blank=True)
    place = models.CharField(verbose_name='거래장소',max_length=20,null=True,blank=True)
    account = models.CharField(verbose_name='계좌',max_length=20,null=True,blank=True)
    content = models.TextField(verbose_name='내용',null=True,blank=True)
    #생성일
    created_at = models.DateTimeField(auto_now_add=True)
    #수정일 (하나의 인스턴스 내용이 변경될 때마다 시간과 날짜 기록)
    updated_at = models.DateTimeField(auto_now=True)
    # 작성자 필드: 글을 작성한 사용자와의 관계를 나타내는 필드
    auth = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)  # 참여할래요

    def total_likes(self):
        return self.likes.count()  # 게시글의 총 추천 수 계산

class Comment(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True) #post로부터 외래키를 가져옴. 게시글 삭제시 댓글도 삭제(on_delete = models.CASCADE)
  body = models.TextField()
  date = models.DateTimeField(auto_now_add=True)