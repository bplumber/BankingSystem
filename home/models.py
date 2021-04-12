from django.db import models

class Customers(models.Model):
    acc_num =  models.IntegerField()
    ifsc = models.TextField()
    name = models.CharField(max_length=100)
    amt = models.IntegerField()

class Transactions(models.Model):
    sacc_num =  models.IntegerField()
    sname = models.CharField(max_length=100)
    racc_num =  models.IntegerField()
    rname = models.CharField(max_length=100)
    amt = models.IntegerField()



