from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

# Create your views here.
def post_create_view(request):
    if request.method == 'POST':
        title = request.POST.get('productName')
        sales= request.POST.get('totalPrice')
        place= request.POST.get('Place')
        account=request.POST.get('userAccount')
        content = request.POST.get('content')
        

        Post.objects.create(
            title = title,
            sales=sales,
            place=place,
            account=account,
            content = content,
    
        )

        return redirect('posts:main')
    # if request.method == 'POST':
    #     form = PostForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         new_post = form.save()
    #         return redirect('main', post_id=new_post.id)  # post_id를 메인 뷰에 전달
    # else:
    #     form = PostForm()

    return render(request, 'writeup.html')

def main_view(request, post_id=None):
    posts = Post.objects.all()
    return render(request, 'main.html', {'posts': posts, 'new_post_id': post_id})