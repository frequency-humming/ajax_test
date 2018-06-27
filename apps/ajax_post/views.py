from django.shortcuts import render, HttpResponse, redirect
from .models import*

# Create your views here.
def index(request):
    if 'id' in request.session:
        return redirect('/post')
    else:
        return render(request,'index.html')

def home(request):
    posts = Post.objects.all() 
    return render(request,"home.html",{'posts': posts})

def user(request):
    if request.method != 'POST':
        return redirect('/')
    else:
        user = User.objects.create(first_name = request.POST['first_name'],last_name = request.POST['last_name'])
        request.session['id'] = user.id
        return redirect('/post')

def create(request):
    if not 'id' in request.session:
        return redirect('/')
    elif request.method != 'POST':
        posts = Post.objects.all() 
        return render(request,'post.html', {'posts': posts})
    else:
        Post.objects.create(content = request.POST['content'], user_posts = User.objects.get(id = request.session['id']))
        posts = Post.objects.all() 
        return render(request,'post.html', {'posts': posts})
    
       
    