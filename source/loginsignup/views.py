from django.shortcuts import render, redirect
from .models import LoginInformation, loginhistory
from django.contrib.auth import authenticate, login as log, logout
from .forms import FirstSignup, Usersignupform, RegistrationForm, AccountAuthenticationForm
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def log_in(request):
    form = FirstSignup(request.POST or None)
    if form.is_valid():
        new_user = form.save()
        #new_user = LoginInformation.objects.create(**form.cleaned_data)
        #authenticated_user = authenticate(username=request.POST['username'], password=request.POST['password'])
        authenticated_user = authenticate(email=new_user.email, password=new_user.password)
        if authenticated_user:
            log(request, authenticated_user)
            return redirect('webpages:homepage')
        else:
            return redirect('webpages:feedback')
    
    context = {'form':form}
    return render(request, 'login1.html', context)

def userlogin(request):
    user = request.user
    if user.is_authenticated:
        return redirect('webpages:homepage')
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                loginhistory.objects.create(useremail=email)
                log(request, user)
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    return redirect('webpages:homepage')
    else:
        form = AccountAuthenticationForm()
    context = {'form':form}
    return render(request, 'login2.html', context)

def logout_view(request):
    logout(request)
    return redirect('webpages:homepage')

def signup(request):
    context = {}
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            loginhistory.objects.create(useremail=email)
            account = authenticate(email=email, password=raw_password)
            log(request, account)
            return redirect('webpages:homepage')
        else:
            context['signup'] = form
    else:
        if request.method != 'POST':
            form = RegistrationForm()
            context['signup'] = form
    return render(request, 'signup.html', context)

def testdiff(request):
    form = FirstSignup(request.POST or None)
    if form.is_valid():
        form.save
    context = {'form':form}
    return render(request, 'test.html', context)

#def signup2(request):
#    form = SecondSignup(request.POST or None)
 #   if form.is_valid():
  #      LoginInformation.objects.create(**form.cleaned_data)
   #     authenticated_user = authenticate(form)
   #     return redirect('webpages:feedback')
    #context = {'form': form}
    #return render(request, 'signup2.html', context)

#def signup3(request):
  #  form = FirstSignup(request.POST or None)
   # if form.is_valid():
    #    first_user = form.save()
     #   authenticated_user = authenticate(username=first_user.username, password=first_user.password)
      #  return redirect('webpages:feedback')
    #context = {'form': form}
    #return render(request, 'signup3.html', context)
