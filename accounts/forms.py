from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()
class LoginFrom(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}) ,label='Tài khoản:', max_length=50)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label='Mật khẩu:', max_length=20)

class RegisterFrom(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label='Tài khoản:', max_length=50)
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}),label='Địa chỉ email:', max_length=50)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label='Mật khẩu:',max_length=20)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label='Xác nhận mật khẩu:',max_length=20)

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username = username)
        if qs.exists():
            raise forms.ValidationError("Tài khoản đã tồn tại.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email = email)
        if qs.exists():
            raise forms.ValidationError("Tài khoản đã tồn tại.")
        return email
    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password != password2:
            raise forms.ValidationError("Mật khẩu không khớp.")
        return data
