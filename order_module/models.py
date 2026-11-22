from django.db import models

# Create your models here.
from account_module.models import User
from product_module.models import Product

class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='user')
    is_paid = models.BooleanField(default=False,verbose_name='is Paid')
    payment_date = models.DateTimeField(blank=True, null= True)
    
    
    def __str__(self):
        return f'user {self.user.get_full_name()}/payment {self.is_paid}'
    
    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'



class Order_details(models.Model):
    product = models.ForeignKey(Product , on_delete=models.CASCADE, verbose_name='Product')
    order = models.ForeignKey(Orders,on_delete= models.CASCADE, verbose_name='Order')
    count = models.PositiveIntegerField(verbose_name='Count')
    final_price = models.PositiveIntegerField(verbose_name='Final unit price',null=True,blank=True)
    
    def __str__(self):
        return f'{self.order}'
    
    def get_total_price(self):
        return self.count * self.product.price
    class Meta:
        verbose_name = 'order details'
        verbose_name_plural = 'order details list'