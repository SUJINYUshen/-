from django.db import models

# Create your models here.
class Department(models.Model):
    """
    部门表
    """
    title = models.CharField(verbose_name='部门名称', max_length=32)
    name = models.CharField(verbose_name='emlpoyee name', max_length=32)
    age = models.IntegerField(verbose_name='emlpoyee age')
    email = models.EmailField(verbose_name='emlpoyee email', max_length=32)
    sex = models.CharField(verbose_name='emlpoyee sex', max_length=4)
    phone = models.CharField(verbose_name='emlpoyee phone', max_length=11)