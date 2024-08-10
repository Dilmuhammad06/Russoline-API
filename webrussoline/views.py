from django.shortcuts import render,redirect, get_object_or_404
from django.views import View
from users.models import User
from .forms import LoginForm, ContentUploadForm, RegisterForm
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from russoline.models import Content, Like
from django.contrib.auth.decorators import login_required

#Auth

class LoginView(View):
    def get(self,request):
        form = LoginForm()
        return render(request,'login.html',{"form":form})

    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid username or password.')
        return render(request,'login.html',{"form":form})

class LogoutView(LoginRequiredMixin,View):
    def get(self,request):
        logout(request)
        return redirect('home')

class RegisterView(View):
    def get(self,request):
        form = RegisterForm()
        return render(request,'register.html',{"form":form})

    def post(self,request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')
        return render(request,'register.html',{"form":form})
    
#Views

class IndexView(View):
    def get(self,request):
        form = ContentUploadForm()
        contents = Content.objects.all().order_by("-created_at")
        return render(request,'index.html',{"contents":contents,"form":form})

    def post(self,request):
        contents = Content.objects.all().order_by("-created_at")
        form = ContentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()

            return redirect('home')
        return render(request,'index.html',{"contents":contents,"form":form})

class ProfileView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'profile.html')

class MessageView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'message.html')

class NotificationView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'notification.html')

class StoriesView(View):
    def get(self,request):
        return render(request, 'stories.html')
    
#Actions

@login_required
def like(request,content_id):
    user = request.user
    content = get_object_or_404(Content, id=content_id)

    existing_like = Like.objects.filter(user=user.id, content=content).exists()

    if not existing_like and user == request.user:
        Like.objects.create(
        user = user,
        content = content
        )
        return redirect("home")
    else:
        Like.objects.filter(user=user.id, content=content).delete()

    return redirect("home")