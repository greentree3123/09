from django.shortcuts import get_object_or_404, render, redirect
from .models import Post

# Create your views here.
def post_create_view(request):
    if request.method == 'POST':
        title = request.POST.get('productName')
        sales= request.POST.get('totalPrice')
        number=request.POST.get('totalNumber')
        place= request.POST.get('Place')
        account=request.POST.get('userAccount')
        content = request.POST.get('content')
        image = request.FILES.get('image')

        post = Post(
            title=title,
            sales=sales,
            number=number,
            place=place,
            account=account,
            content=content,
        )
        try:
            post.image = request.FILES['image']
        except KeyError:
            post.image = None 

        post.save()
        return redirect('posts:main')
    return render(request, 'writeup.html')

def main_view(request, post_id=None):
    posts = Post.objects.all()
    return render(request, 'main.html', {'posts': posts, 'new_post_id': post_id})
    
def post_detail_view(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        return redirect('main')

    context = {
        'post': post,
        'id': id,  
    }
    return render(request, 'myPost.html', context)

def post_update_view(request,id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'GET':
        context = {
            'post': post
        }
        return render(request, 'writeup.html', context)
    else:
        new_image = request.FILES.get('image')
        title = request.POST.get('title')
        sales = request.POST.get('sales')
        place = request.POST.get('place')
        account = request.POST.get('account')
        content = request.POST.get('content')

        if new_image:
            post.image.delete()
            post.image = new_image

        post.title = title
        post.sales = sales
        post.place = place
        post.account = account
        post.content = content
        post.save()
        return redirect('posts:post-detail', post.id)