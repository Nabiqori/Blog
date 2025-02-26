from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .models import *

class HomeView(View):
    def get(self, request):
        if request.user.is_authenticated:
            blogs = Blog.objects.order_by('-sana')
            context = {
                "blogs":blogs,

            }
            return render(request, 'index.html', context)
        return redirect('login')
    def post(self,request):
        if request.user.is_authenticated:
            user = request.user
            muallif = Blog.objects.get(user=user)
            Blog.objects.create(
                sarlavha=request.POST.get('sarlavha'),
                mavzu=request.POST.get('mavzu'),
                matn=request.POST.get('matn'),
                muallif=Muallif.objects.last(),
            )
            return redirect('home')
        return redirect("login")
def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            username=request.POST.get('username'),
            password=request.POST.get('password'),
        )
        if user is not None:
            login(request, user)
            return redirect('home')
        return redirect("login")
    return render(request, "login.html")
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('login')
def register_view(request):
    if request.method == 'POST':
        if request.POST.get('password1') != request.POST.get('password2') or request.POST.get('username') in User.objects.values_list('username', flat=True):
            return redirect("register")
        user = User.objects.create_user(
            username=request.POST.get('username'),
            password=request.POST.get('password1'),
        )
        if user is not None:
            login(request, user)
            return redirect("home")
        return redirect('register')
    return render(request, "register.html")
def blogs_view(request,pk):
    if request.user.is_authenticated:
        blog = Blog.objects.get(id=pk)
        context = {
            "blog":blog,
        }
        return render(request,"blog.html",context)
    return redirect("login")