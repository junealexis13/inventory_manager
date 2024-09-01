from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

##

def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request,"User Logged in!")
            return redirect('mngr-home')
        else:
            messages.error(request,"There was an error logging in. Check login credentials.")
            return redirect('login')
    else:
        return render(request, 'blocks/login_page_blocks.html', context={})

def logout_user(request):
    logout(request)
    messages.success(request,"User successfully logged out.")
    return redirect('login')


