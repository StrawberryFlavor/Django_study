from django.db import models

# Create your models here.
class BookInfo(models.Model):
    """
    图书模型类
    """
    btille = models.CharField(max_length=20)
    # 指定btille为字符串，字符串的最大长度

    bdata = models.DateField()
    #指定bdata为日期类型