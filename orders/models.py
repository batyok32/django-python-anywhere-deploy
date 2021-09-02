from django.db import models
from shop.models import Coupon, Product
from decimal import Decimal
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
  

class Order(models.Model):
    CITIES = (
        ('Ag', 'Ashgabat'),
        ('Ah', 'Ahal'),
        ('Bl', 'Balkan'),
        ('Mr', 'Mary'),
        ('Dz', 'Dasoguz'),
        ('Lb', 'Lebap'),
    )
    full_name=models.CharField("name", max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    email =models.EmailField('email', blank=True, null=True)
    address=models.CharField('address', max_length=250)
    city = models.CharField('city', choices=CITIES, max_length=2)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    coupon = models.ForeignKey(Coupon,
            related_name='orders',
            null=True,
            blank=True,
            on_delete=models.SET_NULL)
    discount = models.IntegerField(default=0,
                validators=[MinValueValidator(0),
                    MaxValueValidator(100)])
    phone_number = models.BigIntegerField('phone_number', validators=[MinValueValidator(99361000000),
                    MaxValueValidator(99365999999)])
    order_notes = models.TextField("order notes")
    is_active = models.BooleanField(default=True)
    total_shop = models.DecimalField(max_digits=10, decimal_places=2,  blank=True, null=True)
    
    class Meta:
        ordering=['-created']

    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost(self):
        total_cost=sum(item.get_cost() for item in self.items.all())
        discount_amount = total_cost * (self.discount / Decimal(100))
        return total_cost - discount_amount

    def get_total_products(self):
        total=self.items.all().count()
        return total

    def save(self, *args, **kwargs):
        self.total_shop = self.get_total_cost()
        super(Order, self).save(*args, **kwargs)
    
class OrderItem(models.Model):
    order=models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product=models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    size=models.CharField(max_length=50)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity