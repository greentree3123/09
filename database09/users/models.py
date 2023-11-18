from django.db import models

# Create your models here.
class Feed(models.Model):
    content = models.TextField()
    image = models.TextField()
    #profile_image = models.TextField()
    #user_id = models.TextField()
    email=models.EmailField(default='') #글쓴이

class Like(models.Model):
    feed_id=models.IntegerField(default=0)
    email = models.EmailField(default='')
    is_like=models.BooleanField(default=True)