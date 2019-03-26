from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index (request):
    # 定义视图函数，HttpRequest
    # http://127.0.0.1:8080/index
    # 进行url配置，建立url地址和视图的对应关系
  return HttpResponse("测试学习")

def myinfo(request):
    return HttpResponse("关于我")