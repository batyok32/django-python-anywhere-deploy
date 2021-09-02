# Models
from django.db import models
from parler.models import TranslatableModel, TranslatedFields

# Utils and Settings
from django.utils import timezone
import datetime
from decimal import Decimal
from django.conf import settings
from django.utils.translation import gettext as _


# Validators
from django.core.validators import MinValueValidator, MaxValueValidator

# Image processors
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill
import contextlib

# File
from django.core.files import File
from django.core.files.storage import default_storage


class Category(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=200, db_index=True),
    )
    slug = models.SlugField(max_length=200,
                            unique=True)
    image = models.ImageField(upload_to='categories/%Y/%m/%d', blank=True, default="product_default.jpg")
    
    # Resize image
    picture = ImageSpecField(
        source="image",
        processors=[ResizeToFill(150, 100)],
        format="WebP",
        options={"quality":100},
    )
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

    def delete(self, *args, **kwargs):
        from django.core.files.storage import default_storage
        if self.image:
            with contextlib.suppress(FileNotFoundError):
                default_storage.delete(
                    self.picture.path
                )
            self.image.delete()
        super().delete(*args, **kwargs)


# Brand Model Table
class Brand(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=100, db_index=True),
    )
    image = models.ImageField(upload_to='brands/%Y/%m/%d', blank=True, default="product_default.jpg")
    category = models.ForeignKey(Category, related_name='brands', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200,
                            unique=True)
    # Resize image
    picture = ImageSpecField(
        source="image",
        processors=[ResizeToFill(150, 100)],
        format="WebP",
        options={"quality":100},
    )
    
    # Return name in admin
    def __str__(self):
        return self.name

    # Meta Headers
    class Meta:
        verbose_name = 'brand'
        verbose_name_plural = 'brands'

    # Delete all images 
    def delete(self, *args, **kwargs):
        from django.core.files.storage import default_storage
        if self.image:
            with contextlib.suppress(FileNotFoundError):
                default_storage.delete(
                    self.picture.path
                )
            self.image.delete()
        super().delete(*args, **kwargs)

# SubCategory Model Table
class Subcategory(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=100, db_index=True),
    )
    
    category = models.ForeignKey(
        Category, related_name='subcategories', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='subcategory/%Y/%m/%d', blank=True, default="product_default.jpg")
    # Resize image
    slug = models.SlugField(max_length=200,
                            unique=True)
    picture = ImageSpecField(
        source="image",
        processors=[ResizeToFill(150, 100)],
        format="WebP",
        options={"quality":100},
    )
    
    # Return name in admin
    def __str__(self):
        return self.name

    # Meta Headers
    class Meta:
        verbose_name = 'subcategory'
        verbose_name_plural = 'subcategories'


# Product Model Table
class Product(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=200, db_index=True),
        description = models.TextField()
    )
   
    new_price = models.DecimalField(
        verbose_name="Price", blank=True, null=True, max_digits=10, decimal_places=2)
    slug = models.SlugField(max_length=200,
                            unique=True)
    category = models.ForeignKey(
        Category, related_name='products', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(
        Subcategory, related_name='products', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.ForeignKey(
        Brand, related_name='products', on_delete=models.CASCADE, null=True, blank=True)
    discount = models.IntegerField(blank=True, null=True,
                                   validators=[MinValueValidator(0),
                                               MaxValueValidator(100)])
    amount = models.IntegerField(default=1)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    sold = models.PositiveIntegerField(blank=True, null=True, default=0)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, default="product_default.jpg")
    # In Big Product
    picture_large = ImageSpecField(
        source="image",
        processors=[ResizeToFill(512, 512)],
        format="WebP",
        options={"quality":100},
    )
    # In Usual Product
    picture_middle = ImageSpecField(
        source="image",
        processors=[ResizeToFill(480, 560)],
        format="WebP",
        options={"quality":100},
    )

    # Using in search 
    picture_search = ImageSpecField(
        source="image",
        processors=[ResizeToFill(120, 90)],
        format="WebP",
        options={"quality":100}
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']

    def get_absolute_url(self):
        return reverse("product_detail", args=[self.id, self.slug])

    # to retrieve is this fresh product

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=4) <= self.created <= now

    # retreive discount
    def get_discount(self):
        if self.discount:
            return (self.discount / Decimal(100)) * self.price
        return Decimal(0)

    # price after discount
    def get_price_after_dis(self):
        if self.discount:
            price = Decimal(self.price - self.get_discount())
            price = f'{price:.2f}'
            price = Decimal(price)
            return price
        # if product does not have discount
        else:
            return self.price

    def delete(self, *args, **kwargs):
        from django.core.files.storage import default_storage
        if self.image:
            with contextlib.suppress(FileNotFoundError):
                default_storage.delete(
                    self.picture_social.path
                )
                default_storage.delete(
                    self.picture_large.path
                )
                default_storage.delete(
                    self.picture_thumbnail.path
                )
            self.image.delete()
        super().delete(*args, **kwargs)

    def get_viewed_count(self):
        self.views_count=self.viewed_users.count()
        return self.views_count


    def save(self, *args, **kwargs):
        if self.amount < 1:
            self.available = False
        if self.category != self.subcategory.category:
            self.category = self.subcategory.category  

        super(Product, self).save(*args, **kwargs)


class Size(models.Model):
    size_name = models.CharField(max_length=50)
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='sizes')
    amount = models.IntegerField(default=1)
    available = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.amount < 1:
            self.available = False
        super(Size, self).save(*args, **kwargs)

class Comment(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='comments')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="comments", on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.user} on {self.product}'


class Contact(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField()
    phone_number = models.IntegerField(validators=[MinValueValidator(61000000),
                                                   MaxValueValidator(65999999)])
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message by {self.name}'


class Coupon(models.Model):
    code = models.CharField(max_length=100, unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount=models.IntegerField(validators=[MinValueValidator(0),
                                            MaxValueValidator(100)])

    active=models.BooleanField(default=True)

    def __str__(self):
        return self.code

    def check_valid(self):
        if self.valid_to <= timezone.now():
            self.active = False
            self.save()
            return False
        return True

    def save(self, *args, **kwargs):
        if self.valid_to <= timezone.now():
            self.active = False
        super(Coupon, self).save(*args, **kwargs)
  
    


