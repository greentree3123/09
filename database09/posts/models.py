from django.db import models


# User=get_user_model()
# Create your models here.
class Post(models.Model):
    image = models.ImageField(verbose_name='이미지',null=True,blank=True)
    title = models.CharField(verbose_name='상품명',max_length=20)
    sales = models.IntegerField(verbose_name='가격')
    number = models.IntegerField(verbose_name='수량',default=0)
    place = models.CharField(verbose_name='거래장소',max_length=20)
    account = models.CharField(verbose_name='계좌',max_length=20)
    content = models.TextField(verbose_name='내용',)
    #생성일
    created_at = models.DateTimeField(auto_now_add=True)
    #수정일 (하나의 인스턴스 내용이 변경될 때마다 시간과 날짜 기록)
    updated_at = models.DateTimeField(auto_now=True)
    # 작성자 필드: 글을 작성한 사용자와의 관계를 나타내는 필드
    #writer = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)