# vending_machine_central

python3==3.8.5
django==3.1.2
djangorestframework==3.12.2



#django_admin startproject xxx
#python3 manage.py runserver
#python3 manage.py migrate      (db)
#python3 manage.py createsuperuser   
#python3 manage.py startapp xxx

#pip install mysqlclient
#pip install djangorestframework

#settings.py 裡面 INSTALLED_APPS=['添加app']
#setting.py 裡面 TEMPLATES=[{'DIRS':['templates'],}]
#setting.py 裡面 
#DATABASES={ 
# 'default': {
#        'ENGINE': 'django.db.backends.mysql',      使用mysql的設定
#        'NAME':'xxx',
#        'USER':'xxx',
#        'PASSWORD':'xxx',
#        'HOST':'localhost',
#        'PORT':'3306',

#    }
#}

#urls.py 裡面  from django.urls import path ,include
#path('',include('mainApp.urls')),
#不要在這裡加url   在app裡面加   這裡直接寫  path('',include('mainApp.urls')),

#App 裡面 admin.py 註冊 models
#from .models import *
#admin.site.register(Product)


#
#
#
#
#
