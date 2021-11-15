from django.db import models
from django.db.models.fields.related import create_many_to_many_intermediary_model

# Create your models here.
class cars(models.Model):
    car_number=models.IntegerField(null=True)


class emp(models.Model):
    emp_name=models.CharField(max_length=100,default="")
    emp_number=models.IntegerField(unique=True, null=True)
    car_id = models.ForeignKey(cars,on_delete=models.CASCADE,null=True )


class project(models.Model):
    p_number=models.IntegerField(unique=True,null=True)
    title=models.CharField(max_length=100,default="")
    emp_id = models.ForeignKey(emp,on_delete=models.CASCADE, null=True)


        



