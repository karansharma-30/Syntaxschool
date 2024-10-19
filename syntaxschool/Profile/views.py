# profile/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate 
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.conf import settings
from django.core.mail import EmailMessage
from django.contrib.auth.models import User 
from django.urls import reverse 
from django.contrib import messages 
from django.utils import timezone



def profile_view(request):
    user_profile = request.user.userprofile
    if request.method == 'POST':
        if 'profile_picture' in request.FILES:
            user_profile.profile_picture = request.FILES['profile_picture']
            user_profile.save()
        # Additional logic for updating bio and other info
        return redirect('profile_view')
    
    return render(request, 'profile/profile.html', {'user_profile': user_profile})

@login_required
def remove_profile_picture(request):
    user_profile = request.user.userprofile
    user_profile.profile_picture.delete()
    user_profile.save()
    return redirect('profile_view')



# Redirect based on authentication status
def profile_redirect_view(request):
    if request.user.is_authenticated:
        return redirect('profile')  # If logged in, go to the profile page
    else:
        return redirect('signup')  # If not logged in, go to the signup page





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
    return render(request, 'profile/login.html', {'form': form})

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
    return render(request, 'profile/signup.html', {'form': form})


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

    return render(request, 'profile/profile.html', {'user_profile': user_profile, 'form': form})




def ForgotPassword(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        try:
            user=User.objects.get(email=email)
            
            new_password_reset=PasswordReset(user=user)
            new_password_reset.save()

            password_reset_url =reverse('reset-password',kwargs={'reset_id': new_password_reset.reset_id})
            full_url = f"{settings.SITE_URL}{password_reset_url}"
            email_body = f"""
        <p>Reset Your Password using the link below:</p>
        <a href="{full_url}">{full_url}</a>
    """
           
            email_message = EmailMessage(
                'Reset your password',
                email_body,
                settings.EMAIL_HOST_USER,
                [email]
            )
            email_message.content_subtype = 'html' 
            email_message.fail_silently=True
            email_message.send()

            return redirect('password-reset-sent', reset_id=new_password_reset.reset_id)
        
        except User.DoesNotExist:
            messages.error(request,f"No user with email '{email}' found")
            return redirect('forgot-password')

    return render(request,'profile/forgot_password.html')




       


def ResetPassword(request, reset_id):
    try:
        password_reset = PasswordReset.objects.get(reset_id=reset_id)

        # Use a fallback value if created_when is None
        if password_reset.created_when is None:
            password_reset.created_when = timezone.now()
            password_reset.save()  # Save the update to the record

        expiration_time = password_reset.created_when + timezone.timedelta(minutes=10)

        # Check if the reset link has expired
        if timezone.now() > expiration_time:
            password_reset.delete()  # Delete expired reset token
            messages.error(request, 'Reset link has expired')
            return redirect('forgot-password')  # Redirect to forgot password page

        if request.method == "POST":
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')

            # Initialize error tracking variable
            password_has_error = False

            # Check if passwords match
            if password != confirm_password:
                password_has_error = True
                messages.error(request, 'Passwords do not match')

            # Check if password is at least 6 characters long
            if len(password) < 6:
                password_has_error = True
                messages.error(request, 'Password must be at least 6 characters long')

            # If no errors, proceed with password reset
            if not password_has_error:
                user = password_reset.user
                user.set_password(password)
                user.save()

                # Delete the reset token after successful reset
                password_reset.delete()

                # Redirect to login page with success message
                messages.success(request, 'Password reset successfully. You can now log in.')
                return redirect('login')

            else:
                # Redirect back to reset page if there are errors
                return redirect('reset-password', reset_id=reset_id)

    except PasswordReset.DoesNotExist:
        # Handle case where reset_id is invalid or doesn't exist
        messages.error(request, "Invalid reset link")
        return redirect('forgot-password')

    # Render the password reset page
    return render(request, 'profile/reset_password.html')       

def passwordResetSent(request,reset_id):
       if PasswordReset.objects.filter(reset_id=reset_id).exists():
           return render(request,'profile/password_reset_sent.html')
       else:
           messages.error(request,"Invalid reset id")
           return redirect('forgot-password')