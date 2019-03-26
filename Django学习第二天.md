### Django的第二天学习记录



通过执行`python manage.py shell`可以进入 shell 终端



#### Django 的后台管理：

**本地化**

- 修改 settings.py 文件

  ```python
  LANGUAGE_CODE = 'zh-hans' # 修改为使用中文
  ```

  ```python
  TIME_ZONE = 'Asia/Shanghai' #使用中国时间
  ```

- 创建管理员

  ```shell
  python manage.py createsuperuser
  ```

- 注册模型类

  在应用下的 admin.py 中注册模型类，告诉django框架根据注册的模型类来生成对应表管理页面

  例：

  ```python
  from django.contrib import admin
  from wind_test.models import BookInfo,HeroInfo
  # Register your models here.
  
  admin.site.register(BookInfo)
  admin.site.register(HeroInfo)
  ```

- 自定义管理页面

  自定义模型管理类。模型管理类就是告诉 django 在生成的管理页面上显示哪些内容

  例：

  ```python
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
  ```



### 视图函数的使用

#### 定义试图函数

视图函数定义在 views.py 中

例：

```python
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index (request):
    # 必须要有一个参数 request ，进行处理之后，需要返回一个 HttpRequest 的类的对象
    # 定义视图函数，HttpRequest
    # http://127.0.0.1:8080/index
    # 进行url配置，建立url地址和视图的对应关系
  return HttpResponse("测试学习")

def myinfo(request):
    return HttpResponse("关于我")
```

#### 进行 url 的配置

建立 url 地址和视图的对应关系

url 配置的目的是让建立 url 和视图函数的对应关系，url 配置项定义在 urlpatterns 列表中，每一个配置项都调用url 函数

配置 url 时，url(正则表达式，include(应用中的 urls 文件))

例：

```python
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)), # 配置项目
    url(r'^',include('wind_test.urls')),

]
```

#### url 匹配的过程

在项目的 urls.py 文件中包含具体应用的 urls.py 文件，应用的 urls.py 文件中写 url 和视图函数的对应关系