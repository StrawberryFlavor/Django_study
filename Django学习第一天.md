## Django 的第一天学习记录

**mvc 的核心思想，解耦，即**：

​	M：Model模型，和数据库进行交互
​	V：View视图，产生html页面
​	C：Controller，控制器,接受请求，进行处理，与 M 和 V 进行交互，返回应答

**Django，MVT，遵循 MVC 分工思想快速开发和DRY原则，Do not repeat yourself，不要让自己去重复一些工作**

### 项目工程文件

- setting.py：项目的配置文件
- urls.py：进行 url 路由的配置
- wsgi.py：服务器和 Django 交互的入口
- manage.py：项目的管理文件

### Django的基本操作

- Django 的环境搭建：`pip install Django==1.8.16`，本次学习指定了1.8.16的版本
- 创建一个 django 的工程：`django-admin startproject $项目名称`
- 创建一个 app 应用：`python manage.py startapp $应用名称`
- 运行一个应用：`python manage.py runserver`
- 模型类生成表，通过`python manage.py make makemigrations`生产迁移文件，产生在`migrations`文件夹下，再执行`python manage.py migrate`执行迁移生成表

·

### 遇到的问题：

当在创建后台 admin 管理员账号时，提示

```
Superuser creation skipped due to not running in a TTY. You can run `manage.py createsuperuser` in your project to create one manually.

```

由于我是在 Git 中使用的，可以在 windows cmd 控制台中重新使用`python manage.py createsuperuser`创建，也可以在 Git Bash 中执行 `winpty python manage.py createsuperuser `