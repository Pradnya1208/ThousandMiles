from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('register')
    else:
        return render(request,'register.html')


def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if User.objects.filter(email=email).exists():
            #return render(request, 'register.html', {'message':'You are already a member of Thousand Miles family!'})
            messages.info(request,'You are already a registered member of Thousand Miles family!')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username already taken register again')
            return redirect('signup')
        if password1 != password2:
            messages.info(request, 'Password mismatch register again')
            return redirect('signup')

        user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name,
                                        last_name=last_name)
        user.save();
        print("user created")
        messages.info(request, 'Registration sucessful ')
        return redirect('register')

    else:
        return render(request, 'signup.html')

def logout(request):
    auth.logout(request)
    return redirect('/')