from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, get_user_model, login, logout
# Create your views here.
def home_page(request):
    context= {

    }
    return render(request,'home_page.html',context)
