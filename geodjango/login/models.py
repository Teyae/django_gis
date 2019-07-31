from django.db import models

# Create your models here


class User(models.Model):
    gender = (('male', "男"), ('female', "女"))
    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default="男")
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):        # 使用__str__方法帮助人性化显示对象信息
        return self.name

    class Meta:                  # 元数据里定义用户按创建时间的反序排列，最近时间的最先显示
        ordering = ["-c_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"


class Spots(models.Model):
    type = (('food', "餐饮"), ('amuse', "娱乐"), ('shopping', "购物"), ('other', "其他"))
    spot_username = models.CharField(max_length=128)
    spot_name = models.CharField(max_length=128, unique=True)
    spot_type = models.CharField(max_length=32, choices=type, default="餐饮")
    spot_lat = models.CharField(max_length=256)
    spot_lon = models.CharField(max_length=256)
    spot_time = models.DateTimeField(auto_now_add=True)
    statement = models.CharField(max_length=256)

    def __str__(self):        # 使用__str__方法帮助人性化显示对象信息
        return self.spot_name

    class Meta:                  # 元数据里定义用户按创建时间的反序排列，最近时间的最先显示
        ordering = ["-spot_time"]
        verbose_name = "SPOT"
        verbose_name_plural = "SPOT"

