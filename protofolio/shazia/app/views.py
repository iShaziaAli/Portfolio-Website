from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'app/index.html')

def posts(request):
    return render(request, 'app/posts.html') 

def post(request):
    return render(request, 'app/post.html')

def profile(request):
    return render(request, 'app/profile.html')    