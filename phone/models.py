from django.db import models
from django.db.models import Choices


# Create your models here.
class Users(models.Model):

    DEPARTMENTS = (
        ('واحد اداری', 'واحد اداری'),
        ('رانندگان', 'رانندگان'),
        ('واحد تولید', 'واحد تولید'),
        ('واحد ای تی', 'واحد ای تی'),
        ('سایر', 'سایر'),
    )

    name = models.CharField(verbose_name='نام', max_length=50)
    phone = models.CharField(verbose_name='شماره دفتر', max_length=50)
    mobile_phone = models.CharField(verbose_name='شماره همراه', max_length=50, blank=True, null=True)
    department = models.CharField(choices= DEPARTMENTS, max_length=50, verbose_name='واحد', default='سایر')

    class Meta:
        verbose_name = 'کارمند'
        verbose_name_plural = 'کارمند ها'

    def __str__(self):
        return self.name