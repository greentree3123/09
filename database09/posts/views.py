from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm, PostSearchForm
from django.db.models import Q
from django.views.generic.edit import FormView

# Create your views here.
def post_create_view(request):
    if request.method == 'POST':
        title = request.POST.get('productName')
        sales= request.POST.get('totalPrice')
        number=request.POST.get('totalNumber')
        place= request.POST.get('Place')
        account=request.POST.get('userAccount')
        content = request.POST.get('content')
        

        Post.objects.create(
            title = title,
            sales=sales,
            number=number,
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

    return render(request, 'main.html', {'posts': posts, 'sort': sort, 'search_query': search_query})

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
