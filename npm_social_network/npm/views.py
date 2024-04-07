from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import HttpResponse


def index(request):
    return render(request, 'npm/index.html')

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already exists")
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists")
                return redirect('register')
            else:
                user = User.objects.create_user(email=email, username=username, password=password)
                user.save()
                messages.info(request, "Registered sucessfully")
                return render(request, 'npm/login.html')
        else:
            messages.info(request, "Passwords do not match")
            return redirect('register')
    else:
        messages.info(request, "There is a problem is sign up")
        return render(request, 'npm/register.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, "Invalid credentials")
            return render(request, 'npm/login.html') 
    else:
        return render(request, 'npm/login.html') 
    
@login_required
def logout(request):
    auth.logout(request)
    return redirect('login')
    

@login_required 
def dashboard(request):
    return render(request, 'npm/dashboard.html')  

# def register(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return render(request, 'npm/login.html', {'success': "Registration successful. Please login."})
#         else:
#             error_message = form.errors.as_text()
#             return render(request, 'npm/register.html', {'error': error_message})

#     return render(request, 'npm/register.html')

# from django.contrib.auth.models import User

# def user_login(request):
#     if request.method == "POST":
#         email = request.POST.get('email')
#         password = request.POST.get('password')
        
#         # Query the database for the user
#         try:
#             user = User.objects.get(email=email)
#         except User.DoesNotExist:
#             user = None

#         if user is not None and user.check_password(password):
#             # User exists and password is correct
#             login(request, user)
#             return redirect("dashboard")
#         else:
#             # Invalid credentials
#             return render(request, 'npm/login.html', {'error': "Invalid credentials. Please try again."})

#     return render(request, 'npm/login.html')


# @login_required
# def dashboard(request):
#     return render(request, 'npm/dashboard,html', {'name': request.user.first_name})

# def user_logout(request):
#     pass 

@login_required
def profile(request):
    render(request, 'npm/profile.html')

def about(reques):
    return HttpResponse('About')

def policy(request):
    return HttpResponse('Policy')