from django.shortcuts import render, redirect
from .forms import LoginFrom, RegisterFrom
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.utils.http import is_safe_url
# Create your views here.
def login_page(request):
    form = LoginFrom(request.POST or None)
    context = {
        'form':form
    }
    print("User logged in")
    next_ =request.GET.get('next')
    next_post =request.POST.get('next')
    redirect_path = next_ or next_post or None
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect("/")
        else:
            print("Error")
    return render(request,'auth/login.html',context)
User = get_user_model()
def register_page(request):
    form = RegisterFrom(request.POST or None)
    context = {
        'form':form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)
        print(new_user)
    return render(request,'auth/register.html',context)

def logout_page(request):
    print(request.path)
    logout(request)
    return redirect('/')
