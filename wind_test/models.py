from django.db import models
# 设计和表对应的类

# Create your models here.
class BookInfo(models.Model):
    """
    图书模型类
    """
    btille = models.CharField(max_length=20)
    # 指定btille为字符串，字符串的最大长度

    bdata = models.DateField()
    #指定bdata为日期类型

class HeroInfo(models.Model):
    """
    英雄属性模型类
    """
    heroname = models.CharField(max_length=20)
    # 英雄名称
    herogender =models.BooleanField(default=False)
    # 性别，bool类型，False代表男，默认值为男
    herocomment = models.CharField(max_length=128)
    # 备注
    herobook = models.ForeignKey('BookInfo')
    # herobook，建立图书类贺英雄人物类之间的一对多关系，对应关系关系属性名_id，外键

