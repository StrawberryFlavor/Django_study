from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,RequestContext
from wind_test.models import BookInfo
# Create your views here.

def my_render(temp_path,request,context_dict={}):
    """
    自己尝试封装模板方法，其实导入过来的 render 已经做了处理了
    :return:
    """
    temp = loader.get_template(temp_path) #加载模版
    context = RequestContext(request,context_dict) # 定义模版上下文
    respone_html = temp.render(context) #模版渲染
    return HttpResponse(respone_html)


def index (request):
    # 定义视图函数，HttpRequest
    # http://127.0.0.1:8080/index
    # 进行url配置，建立url地址和视图的对应关系
  # return HttpResponse("测试学习")

    # 使用模板文件
    # 加载模板文件
    # temp =loader.get_template('wind_test/index.html')# 返回一个模板对象
    # # 定义模板上下文：给模板文件传递数据
    # context =RequestContext(request,{''})
    # # 模板渲染：产生标准的 html 内容
    # respone_html = temp.render(context)
    # return HttpResponse(respone_html)、
    # return my_render('wind_test/index.html',request)
    index_dict ={'content':'hello word','list':list(range(1,100))}
    return render(request,'wind_test/index.html',index_dict)


def show_books(request):
    """
    定义books的视图函数

    """
    # 通过models查找图书表中的数据
    books = BookInfo.objects.all()
    show_books_dict ={'books':books}
    return render(request,'wind_test/show_books.html',show_books_dict)

def detail(request,bid):
    """
    查询图书关联的英雄信息
    """
    # 根据id查询图书信息
    books = BookInfo.objects.get(id=bid)
    # 查询和book关联的英雄信息
    heros = books.heroinfo_set.all()
    detail_book_dict = {'books':books,'heros':heros}
    return render(request,'wind_test/detail.html',detail_book_dict)

def myinfo(request):
    return HttpResponse("关于我")