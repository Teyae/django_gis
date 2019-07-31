from django import forms


class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Username", 'autofocus': ''}))
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Password"}))


class RegisterForm(forms.Form):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="确认密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label='性别', choices=gender)


class SpotsForm(forms.Form):
    type = (('food', "餐饮"), ('amuse', "娱乐"), ('shopping', "购物"), ('other', "其他"))
    spot_name = forms.CharField(label="商铺名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    spot_type = forms.ChoiceField(label='商铺类型', choices=type)
    statement = forms.CharField(label="心店记录", max_length=256, widget=forms.TextInput(attrs={'class': 'form-control'}))