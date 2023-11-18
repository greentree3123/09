from uuid import uuid4
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Feed,Like
from user.models import User
import os
from database09.settings import MEDIA_ROOT
class Main(APIView):
    def get(self,request):

        email = request.session.get('email', None)
        if email is None:
            return render(request, "user/login.html")
        user = User.objects.filter(email=email).first()
        if user is None:
            return render(request, "user/login.html")
        feed_object_list=Feed.objects.all().order_by('-id')#쿼리셋;select *from content_feed;와 같음, order by 는 최신순으로 피드업데이트하려고
        feed_list=[]
        for feed in feed_object_list:
            user=User.objects.filter(email=feed.email).first()

            like_count= Like.objects.filter(feed_id=feed.id,is_like=True).count()
            is_liked=Like.objects.filter(feed_id=feed.id,email=email,is_like=True).exists()
            feed_list.append(dict(id=feed.id,
                                  image=feed.image,
                                  content=feed.content,
                                  like_count=like_count,
                                  profile_image=user.profile_image,
                                  nickname=user.nickname,
                                  is_liked=is_liked,

                                  ))

            feed.email


        return render(request,"hakseat/main.html",context=dict(feeds=feed_list,user=user))
class UploadFeed(APIView):
    #일단 파일을 불러와
    def post(self,request):
        file = request.FILES['file']
        uuid_name = uuid4().hex
        save_path = os.path.join(MEDIA_ROOT, uuid_name)

        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        file = request.data.get('file')
        image =uuid_name
        content = request.data.get('content')
        email = request.session.get('email', None)
        Feed.objects.create(image=image,content=content,email=email)

        return Response(status=200)
class Profile(APIView):
    def get(self,request):
        email = request.session.get('email', None)
        if email is None:
            return render(request, "user/login.html")
        user = User.objects.filter(email=email).first()
        if user is None:
            return render(request, "user/login.html")

        feed_list=Feed.objects.filter(email=email)
        like_list=list(Like.objects.filter(email=email,is_like=True).values_list('feed_id',flat=True))
        like_feed_list=Feed.objects.filter(id__in=like_list)


        return render(request,'content/profile.html',context=dict(feed_list=feed_list,
                                                                  user=user,
                                                                  like_feed_list=like_feed_list,
                                                                   ))



class ToggleLike(APIView):
    def post(self,request):
        feed_id=request.data.get('feed_id',None)
        favorite_text=request.data.get('favorite_text',True)
        if favorite_text=='favorite_border':
            is_like=True
        else:
            is_like=False
        email = request.session.get('email', None)
        like=Like.objects.filter(feed_id=feed_id,email=email).first()
        if like:
            like.is_like=is_like
            like.save()
        else:
            Like.objects.create(feed_id=feed_id,is_like=is_like,email=email)

        return Response(status=200)

class Seeat(APIView):
    def get(self,request):
        feed_object_list = Feed.objects.all().order_by(
            '-id')  # 쿼리셋;select *from content_feed;와 같음, order by 는 최신순으로 피드업데이트하려고
        feed_list = []
        for feed in feed_object_list:
            user = User.objects.filter(email=feed.email).first()

            like_count = Like.objects.filter(feed_id=feed.id, is_like=True).count()
            #is_liked = Like.objects.filter(feed_id=feed.id, email=email, is_like=True).exists()
            feed_list.append(dict(id=feed.id,
                                  image=feed.image,
                                  content=feed.content,
                                  like_count=like_count,
                                  profile_image=user.profile_image,
                                  nickname=user.nickname,
                                  #is_liked=is_liked,

                                  ))



        return render(request,'content/seeat.html',context=dict(feeds=feed_list,user=user))
