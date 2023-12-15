from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from .token import user_tokenizer_generate

from django.contrib.auth.models import User
from .forms import CreateUserForm, LoginForm, UpdateUserForm

from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = False
            user.save()

            # - Email verification setup 
            current_site = get_current_site(request)
            subject = "Activate your account"
            message = render_to_string('account/registration/email_verification.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': user_tokenizer_generate.make_token(user),
            })

            user.email_user(subject=subject, message=message)

            return redirect('email_verification_sent')

    return render(request, 'account/registration/register.html', {
        'form': form,
    })


def email_verification(request, uidb64, token):
    uid = force_str(urlsafe_base64_decode(uidb64))
    user = User.objects.get(pk=uid)

    if user and user_tokenizer_generate.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('email_verification_success')
    else:
        return redirect('email_verification_failed')


def email_verification_sent(request):
    return render(request, 'account/registration/email_verification_sent.html')


def email_verification_success(request):
    return render(request, 'account/registration/email_verification_success.html')


def email_verification_failed(request):
    return render(request, 'account/registration/email_verification_failed.html')


def login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            
            if user:
                auth.login(request, user)
                return redirect('dashboard')
    
    return render(request, 'account/my_login.html', {
        'form': form,
    })


def logout(request):
    auth.logout(request)
    return redirect('store')


@login_required(login_url='login')
def dashboard(request):
    return render(request, 'account/dashboard.html')


@login_required(login_url='login')
def profile_manage(request):
    form = UpdateUserForm(instance=request.user)
    
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=request.user)
        if form.is_valid(): 
            form.save()
            return redirect('dashboard')

    return render(request, 'account/profile_management.html', {
        'form': form,
    })


@login_required(login_url='login')
def account_delete(request):
    if request.method == 'POST':
        user = User.objects.get(pk=request.user.pk)
        user.delete()
        return redirect('store')

    return render(request, 'account/delete_account.html')