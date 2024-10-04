# profile/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserSignupForm, UserProfileForm , UserLoginForm
from .models import UserProfile
from .forms import UserProfileForm 
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout





def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)


        if request.user.is_authenticated:
                  return redirect('profile')  # Redirect to profile if already logged in
    # rest of the code...
        
        elif form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('profile')  # Redirect to profile page
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

# profile/views.py
@login_required
def logout_view(request):
    auth_logout(request)
    return redirect('login')  # Redirect to the login page


def signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            UserProfile.objects.create(user=user)  # Create a user profile
            login(request, user)  # Log the user in
            return redirect('profile')  # Redirect to profile page
    else:
        form = UserSignupForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def profile_view(request):
    user = request.user
    
    # Try to get the user profile, if it doesn't exist, create one
    try:
        user_profile = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        user_profile = UserProfile(user=user)  # Create a new user profile
        user_profile.save()

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the same profile view or wherever you like
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'profile.html', {'user_profile': user_profile, 'form': form})
