from . import forms
from . import models
from django.shortcuts import render
from django.shortcuts import redirect
import re

from django.core import serializers

# Create your views here.


def index(request):                   # 都是函数，接受request参数，返回render结果
    if request.method == 'POST':

        spot_name = request.POST.get('spot_name')
        spot_type = request.POST.get('spot_type')
        statement = request.POST.get('statement')
        spot_lat = request.POST.get('spot_lat')
        spot_lon = request.POST.get('spot_lon')
        spot_username = request.user

        new_spot = models.Spots()
        new_spot.spot_username = spot_username
        new_spot.spot_name = spot_name
        new_spot.spot_type = spot_type
        new_spot.statement = statement
        new_spot.spot_lat = spot_lat
        new_spot.spot_lon = spot_lon

        new_spot.save()

        return redirect('/index/')

    p = r"'([^']+)'"

    search_name = models.Spots.objects.values_list('spot_name')
    select_name = list(search_name)
    re_select_name = list(map(lambda x: re.search(p, str(x)).group(1), select_name))

    search_statement = models.Spots.objects.values_list('statement')
    select_statement = list(search_statement)
    re_select_statement = list(map(lambda x: re.search(p, str(x)).group(1), select_statement))

    search_lon = models.Spots.objects.values_list('spot_lon')
    select_lon = list(search_lon)
    re_select_lon = list(map(lambda x: re.search(p, str(x)).group(1), select_lon))

    search_lat = models.Spots.objects.values_list('spot_lat')
    select_lat = list(search_lat)
    re_select_lat = list(map(lambda x: re.search(p, str(x)).group(1), select_lat))

    # search_lat = serializers.serialize("json", models.Spots.objects.only('spot_lat'))
    # search_lon = serializers.serialize("json", models.Spots.objects.only('spot_lon'))

    spot_list = list(models.Spots.objects.all())
    return render(request, 'login/index.html', locals()) # {'events': serializers.serialize("json", 'search_lon', fields='spot_lon')})# 'events2': serializers.serialize("json", 'search_lat', fields='spot_lat')})


def login(request):
    if request.session.get('is_login', None):  # 不允许重复登录
        return redirect('/index/')
    if request.method == 'POST':
        login_form = forms.UserForm(request.POST)
        message = '请检查填写的内容！'
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')

            try:
                user = models.User.objects.get(name=username)
            except :
                message = '用户不存在！'
                return render(request, 'login/login.html', locals())

            if user.password == password:                 # 写入用户状态和数据
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                return redirect('/index/')
            else:
                message = '密码不正确！'
                return render(request, 'login/login.html', locals())
        else:
            return render(request, 'login/login.html', locals())

    login_form = forms.UserForm()
    return render(request, 'login/login.html', locals())


def register(request):
    if request.session.get('is_login', None):
        return redirect('/index/')

    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            email = register_form.cleaned_data.get('email')
            sex = register_form.cleaned_data.get('sex')

            if password1 != password2:
                message = '两次输入的密码不同！'
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:
                    message = '用户名已经存在'
                    return render(request, 'login/register.html', locals())
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:
                    message = '该邮箱已经被注册了！'
                    return render(request, 'login/register.html', locals())

                new_user = models.User()
                new_user.name = username
                new_user.password = password1
                new_user.email = email
                new_user.sex = sex
                new_user.save()

                return redirect('/login/')
        else:
            return render(request, 'login/register.html', locals())
    register_form = forms.RegisterForm()
    return render(request, 'login/register.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/login/")
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/login/")


