from django.contrib import admin
from wind_test.models import BookInfo,HeroInfo
# Register your models here.


class BookInfoAdmin(admin.ModelAdmin):
    """
    图书模型管理类
    """
    list_display = ['id','btille','bdata']

class HeroInfoAdmin(admin.ModelAdmin):
    """
    英雄模型类管理类
    """
    list_display = ['id','heroname','herogender','herocomment','herobook']

admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)