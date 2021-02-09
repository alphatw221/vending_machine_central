from django.contrib import admin

# Register your models here.
#在這裡設定models

from .models import *

admin.site.register(Product)
admin.site.register(Transaction)
admin.site.register(Restock)
admin.site.register(Machine)