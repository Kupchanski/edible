from django import forms
from django.contrib.auth import (
  authenticate,
  get_user_model,
  login,
  logout,)
User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        #
        # user_qs = User.objects.filter(username=username)
        # # if user_qs.count() == 0:
        # #     raise forms.ValidationError("Пользователь не найден\Неверный пароль")
        # # else:
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError("Пользователь не найден\Неверный пароль")
        if not user.check_password(password):
            raise forms.ValidationError("Пользователь не найден\Неверный пароль")
        if not user.is_active:
            raise forms.ValidationError("Данный пользователь более не активен. Обратитесь к администрации сайта")
        return super(UserLoginForm, self).clean(*args, *kwargs)


class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label="Введите email")
    email2 = forms.EmailField(label="Подтвердите email")
    password = forms.CharField(widget=forms.PasswordInput,label="Введите пароль")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Подтвердите пароль")

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password',
            'password2'
        ]

    def clean_email2(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError("Email не совпадает")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email уже используется")
        return email

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("Пароли не совпадают")
        return password
