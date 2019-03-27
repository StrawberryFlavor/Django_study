### Django 的第三天学习记录



模板不仅仅是一个 html 文件



#### 模板文件的使用

- 在项目中创建模板文件夹，对应的应用模版文件夹

- 配置模板目录

  ```python
  TEMPLATES = [
      {
          'BACKEND': 'django.template.backends.django.DjangoTemplates',
          'DIRS': [os.path.join(BASE_DIR,'templates')], # 路径拼接
          'APP_DIRS': True,
          'OPTIONS': {
              'context_processors': [
                  'django.template.context_processors.debug',
                  'django.template.context_processors.request',
                  'django.contrib.auth.context_processors.auth',
                  'django.contrib.messages.context_processors.messages',
              ],
          },
      },
  ]
  ```

- 使用模板文件

  - 加载模板文件：去模板目录下面获取 html 文件的内容 ，得到一个模板对象
  - 定义模板上下文：向模板文件传递数据
  - 模板渲染：得到一个标准的 html 内容

  

  

  

  #### 给模版文件传递数据

  模版变量使用：{{ 模版变量名 }}

  模版代码段：{% 代码段%}

  for 循环：

  {% for i in list%}

  {% endfor%}

