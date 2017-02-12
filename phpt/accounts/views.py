from django.shortcuts import render, redirect
from django.core.mail import  send_mail
from django.conf import settings
from django.contrib.auth import (
  authenticate,
  get_user_model,
  login,
  logout,)

from .forms import UserLoginForm, UserRegisterForm, ContactForm


def home_view(request):
    return render(request, "home.html", {})


def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/')

    return render(request, "form.html", {"form":form})


def register_view(request):
    title = "Регистрация"
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request,new_user)
        return redirect('/')

    return render(request, "form.html", {"form":form})


def logout_view(request):
    logout(request)
    return redirect('/')


def contact_view(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get("email")
        message = form.cleaned_data.get('message')
        name = form.cleaned_data.get('name')
        subject = 'Garnet Cart contact form'
        from_email = settings.EMAIL_HOST_USER
        contact_message = "Сообщение от %s:\n \'%s\'. \n" \
                          "Обратная почта: %s"%(name, message,email)
        to_email = [from_email, 'kirich_s4@mail.ru']
        send_mail(subject,
                  contact_message,
                  from_email,
                  to_email,
                  fail_silently=False)

    return render(request, "form.html", {"form" : form})


def about_view(request):
    pass
