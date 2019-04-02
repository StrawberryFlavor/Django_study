## Django 的第五天学习记录

#### Django 数据库的配置

在`settings`中的`DATABASES`中，将`ENGINE`中的`sqlite3`改为要使用的关系型数据库，如`mysql`

```python
'ENGINE':'django.db.backends.mysql'
```

将`NAME`改为数据库的名字 ,例如库的名字为 `study`

```python
'NAME':'study' #使用的数据库的名字,数据库必须手动创建
```

并写上数据库的用户名和密码，连接地址和端口

```python
'USER':'root' #链接 mysql 的用户名
'PASSWORD'：'mysql' #用户对应的密码
'HOST':'localhost' #指定 mysql 数据库所在电脑的ip
'PORT':'3306' #mysql 的端口号
```



下载模块包：`pip install pymysql`



在项目的初始文件中加入内容

```python
import pymysql
pymysql.install_as_MySQLdb()
```

