from django.contrib.auth.models import AbstractUser

from django.db import models

class User(AbstractUser):
    mobile = models.CharField(max_length=10,verbose_name='mobile', null=True, blank=True)
    email_active_code = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=True,null=False, blank=False)
    avatar= models.ImageField(upload_to='images/avatar', verbose_name='Avatar', blank=True, null=True)
    address = models.TextField(verbose_name='Address',blank=True, null=True)
    about = models.TextField(verbose_name='about',blank=True, null=True)
    class Meta:
        db_table = 'Users'
        verbose_name = 'user'
        verbose_name_plural ='users'