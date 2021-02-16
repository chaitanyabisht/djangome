from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def firstgame(request):
    return render(request,'mypage.html')

def hobbies(request):
    return render(request,'hobbies.html')

def plans(request):
    return render(request,'mypage.html')