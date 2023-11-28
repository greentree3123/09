from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

# Create your views here.
def post_create_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            new_post = form.save()
            return redirect('main', post_id=new_post.id)  # post_id를 메인 뷰에 전달
    else:
        form = PostForm()

    return render(request, 'writeup.html', {'form': form})

def main_view(request, post_id=None):
    posts = Post.objects.all()
    return render(request, 'main.html', {'posts': posts, 'new_post_id': post_id})