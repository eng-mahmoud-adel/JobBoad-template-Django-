from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SignupForm, UserForm, ProfileForm
from .models import Profile
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            # get username and password to login
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            # create a session to login and make the user authenticated
            user = authenticate(username=username, password=password)
            # login
            login(request, user)
            return redirect('accounts/profile.html')
                
    else:
        form = SignupForm()

    return render(request, 'registration/signup.html', {
        'form': form
    })


# @login_required
def profile(request):
    # get the curret logged-in user
    profile = Profile.objects.get(user=request.user)

    return render(request, 'accounts/profile.html', {
        'profile': profile
    })

# @login_required
def edit_profile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        userForm = UserForm(request.POST, instance=request.user)
        profileForm = ProfileForm(request.POST, request.FILES, instance=profile)

        if userForm.is_valid() and profileForm.is_valid():
            userForm.save()
            profileForm.save()
            return redirect(reverse('profile'))

    else:
        userForm = UserForm(instance=request.user)
        profileForm = ProfileForm(instance=profile)

    return render(request, 'accounts/edit_profile.html', {
        'userForm': userForm,
        'profileForm': profileForm,
    })
    pass