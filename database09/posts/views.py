from django.shortcuts import get_object_or_404, render, redirect
from .models import Comment, Post
from .forms import PostForm, PostSearchForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView

# Create your views here.
@login_required
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
            auth=request.user
        )
        try:
            post.image = request.FILES['image']
        except KeyError:
            post.image = None 

        post.save()
        return redirect('posts:main')
    return render(request, 'writeup.html')

def main_view(request, post_id=None):
    sort = request.GET.get('sort')

    if sort == 'price':
        posts = Post.objects.all().order_by('sales')  # 가격 낮은 순
    elif sort == 'recently':
        posts = Post.objects.all().order_by('-created_at')  # 최신순
    elif sort == 'likes':
        posts = Post.objects.all().order_by('-likes')  # 인기순
    else:
        posts = Post.objects.all()

    search_query = request.GET.get('search')
    if search_query:
        posts = posts.filter(Q(title__icontains=search_query) | Q(content__icontains=search_query))
    return render(request, 'main.html', {'posts': posts, 'new_post_id': post_id, 'sort': sort, 'search_query': search_query})

def post_detail_view(request, id):
    try:
        post = Post.objects.get(id=id)
        comments = Comment.objects.filter(post=post)

        if request.method == 'POST':
            new_image = request.FILES.get('image')
            title = request.POST.get('productName')
            sales = request.POST.get('totalPrice')
            number = request.POST.get('totalNumber')
            place = request.POST.get('Place')
            account = request.POST.get('userAccount')
            content = request.POST.get('content')

            if new_image:
                post.image.delete()
                post.image = new_image

            post.title = title
            post.sales = sales
            post.number = number
            post.place = place
            post.account = account
            post.content = content
            post.save()

            body = request.POST.get('body')
            Comment.objects.create(post=post, body=body)

    except Post.DoesNotExist:
        return redirect('main')

    context = {
        'post': post,
        'id': id,
        'comments': comments,
    }
    return render(request, 'myPost.html', context)

@login_required
def post_update_view(request,id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'GET':
        context = {
            'post': post
        }
        return render(request, 'writeup.html', context)
    else:
        new_image = request.FILES.get('image')
        title = request.POST.get('productName')
        sales = request.POST.get('totalPrice')
        number = request.POST.get('totalNumber')
        place = request.POST.get('Place')
        account = request.POST.get('userAccount')
        content = request.POST.get('content')

        if new_image:
            post.image.delete()
            post.image = new_image

        post.title = title
        post.sales = sales
        post.number = number
        post.place = place
        post.account = account
        post.content = content
        post.save()
        return redirect('posts:main')
    
def post_list_view(request):
    sort = request.GET.get('sort')

    if sort == 'sales':
        post_list = Post.objects.all().order_by('sales_count')  
   
    else:
        posts = Post.sales.all()

    return render(request, 'main.html', {'posts': posts, 'sort': sort})

class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'main.html'

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        post_list = Post.objects.filter(Q(title__icontains=searchWord) | Q(description__icontains=searchWord) | Q(content__icontains=searchWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = post_list

        return render(self.request, self.template_name, context)