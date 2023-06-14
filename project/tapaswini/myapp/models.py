from django.db import models

# Create your models here.

# class coursemanager(models.Manager):
#     def sort_desc_price(a):
#         return a.order_by('cprice').all()
# class Itvedant(models.Model):
#     cname=models.CharField(max_length=50)
#     cdur=models.IntegerField(max_length=15)
#     cprice=models.IntegerField(max_length=20)
#     #c_manager=models.Manager()


class Employee(models.Model):
    name = models.CharField(max_length=90)
    designation = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    join_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name