from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from .forms import registerForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

def registerView(request):
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Accounts was created for ' + username)
            return redirect('/')
    else:
        form = registerForm()
    context= {'forms':form}
    return render(request, 'users/register.html',context)

def loginView(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password = password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    return render(request,'users/login.html')

def logoutView(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def profileView(request):
    # below the request checks for the updateing the values
    # instance = request.user) means it shows current user details
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profilemodel)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Account was updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profilemodel)

    context = {
            'u_form': u_form,
            'p_form':p_form

    }
    return render(request,'users/profile.html',context)
