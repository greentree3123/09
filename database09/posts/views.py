from django.shortcuts import render, redirect
from .forms import PostForm

# Create your views here.
def post_create_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'main.html')
    else:
        form = PostForm()

    return render(request, 'writeup.html', {'form': form})