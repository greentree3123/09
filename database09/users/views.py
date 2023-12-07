from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect

from users.models import User

#로그인
def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        
        # Authenticate the user
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            # Check if the user is registered (if not, you can redirect to signup)
            login(request, user)
            return redirect('posts:main')  # Redirect to main view after successful login
        else:
            # Handle invalid login credentials
            # You might want to add a message to the user here
            pass

    return render(request, 'login.html')


def signup_view(request):
    if request.method == "GET":
        return render(request, 'signup.html')
    elif request.method =="POST":
        email = request.POST.get('email', None)
        nickname = request.POST.get('nickname', None)
        name = request.POST.get('name', None)
        password = request.POST.get('password', None)
        
        User.objects.create(email=email,
                            nickname=nickname,
                            name=name,
                            password=make_password(password),
                            profile_image="Vector.png")
        return redirect('users:login')
    return render(request, 'signup.html')

def profile(request):
    return render(request, 'profile.html')

