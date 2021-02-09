from django.db import models


#確認已經把app加進setting 再做migrate
#要道admin裡面 註冊才會出現
#python3 manage.py makemigrations
#python3 manage.py migrate

class Machine(models.Model):

    name=models.CharField(max_length=30)
    location=models.CharField(max_length=40)

    # products=models.ManyToManyField(Product,blank=True, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):

    name=models.CharField(max_length=30)
    sale_price=models.IntegerField()
    purchase_price=models.IntegerField()
    stock=models.IntegerField()
    description=models.TextField(blank=True, null=True)
    
    machines=models.ManyToManyField(Machine,related_name='products',blank=True, null=True)

    def __str__(self):
        return self.name


class Transaction(models.Model):

    product=models.ForeignKey('Product',related_name='transactions',on_delete=models.DO_NOTHING)
    machine=models.ForeignKey('Machine',related_name='transactions',on_delete=models.DO_NOTHING)
    revenue=models.IntegerField(default=None)
    profit=models.IntegerField(default=None)
    amount=models.IntegerField()

    dateTime=models.DateField()
    

    def __str__(self):
        return str('id:')+str(self.id)
    

class Restock(models.Model):

    product=models.ForeignKey('Product',related_name='restocks',on_delete=models.DO_NOTHING)
    machine=models.ForeignKey('Machine',related_name='restocks',on_delete=models.DO_NOTHING)

    
    amount=models.IntegerField()
    value=models.IntegerField(default=None)
    dateTime=models.DateField()
    

    def __str__(self):
        return str('id:')+str(self.id)
