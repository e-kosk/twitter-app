from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView

from twitter.forms import NewTweetForm, LoginForm, RegisterForm
from twitter.models import Tweet


class HomeView(View):

    def get(self, request):
        tweets = Tweet.objects.all()
        new_tweet_form = NewTweetForm()
        context = {
            'tweets': tweets,
            'new_tweet_form': new_tweet_form,
        }
        return render(request, 'twitter/home.html', context)

    def post(self, request):
        tweets = Tweet.objects.all()
        new_tweet_form = NewTweetForm(request.POST)
        context = {
            'tweets': tweets,
            'new_tweet_form': new_tweet_form,
        }
        if new_tweet_form.is_valid():
            Tweet.objects.create(content=request.POST.get('content'), owner=request.user)
            return redirect('/')
        return render(request, 'twitter/home.html', context)


class LoginView(View):

    def get(self, request):
        login_form = LoginForm()
        context = {
            'login_form': login_form
        }
        return render(request, 'base/login.html', context)

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['login']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('/')
        return render(request, 'base/login.html', {'login_form': login_form})


def logout_view(request):
    logout(request)
    return redirect('/login')


class MessagesView(View):
    pass


class AccountView(View):

    def get(self, request):
        user = request.user
        user_tweets = Tweet.objects.filter(owner=user)
        context = {
            'user': user,
            'user_tweets': user_tweets,
        }
        return render(request, 'twitter/account.html', context)


class TweetInfoView(View):
    pass


class RegisterView(View):

    def get(self, request):
        register_form = RegisterForm()
        context = {
            'register_form': register_form,
        }
        return render(request, 'twitter/register.html', context)

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            if register_form.cleaned_data.get('password1') == register_form.cleaned_data.get('password2'):
                username = register_form.cleaned_data.get('username'),
                first_name = register_form.cleaned_data.get('first_name'),
                last_name = register_form.cleaned_data.get('last_name'),
                email = register_form.cleaned_data.get('email'),
                password = register_form.cleaned_data.get('password1'),
                User.objects.create_user(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=password,
                )
                user = authenticate(username=username, password=password)
                if user:
                    login(request, user)
                    return redirect('/')
        return render(request, 'twitter/register.html', {'register_form': register_form})
