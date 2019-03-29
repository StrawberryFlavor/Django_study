from django.conf.urls import url
from wind_test import views

urlpatterns = [
    # 通过url函数设置url路由配置项
    url(r'^index',views.index),# 建立/index和视图index之间的关系
    url(r'^myinfo',views.myinfo),
    url(r'^books',views.show_books),
    url(r'^book/(\d+)$',views.detail),

]