# Models
from shop.models import  Comment
from orders.models import Order

# Mixins
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, PermissionsMixin, BaseUserManager

# Validators
from django.core.validators import MinValueValidator, MaxValueValidator

# Settings and utils
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from django.apps import apps

# Image processors
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill


class UserAccountManager(BaseUserManager):
    def _create_user(self, username, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError("Users must haven a name")

        username = self.model.normalize_username(username)

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, password, **extra_fields)


class UserAccount(AbstractBaseUser, PermissionsMixin):
    CITIES = (
        ('Ag', 'Ashgabat'),
        ('Bl', 'Balkan'),
        ('Mr', 'Mary'),
        ('Dz', 'Dasoguz'),
        ('Lb', 'Lebap'),
    )
    email = models.EmailField(
        max_length=255, blank=True, null=True)
    username = models.CharField(
        max_length=255, unique=True)

    phone_number = models.BigIntegerField('Phone Number',
                                          unique=True,
                                          validators=[MinValueValidator(99361000000),
                                                      MaxValueValidator(
                                                          99365999999)],
                                          error_messages={
                                              'unique': "A user with that phone number already exists.",
                                          },)
    address = models.TextField(
        'address', max_length=250, blank=True, null=True)
    city = models.CharField('city', choices=CITIES,
                            max_length=2, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    profile_img = models.ImageField(upload_to='users/%Y/%m/%d', blank=True, default="default-icon.jpg")
    profile_social = ImageSpecField(
        source="profile_img",
        processors=[ResizeToFill(512, 512)],
        format="WebP",
        options={"quality":100},
    )
    
    profile_avatar = ImageSpecField(
        source="profile_img",
        processors=[ResizeToFill(40, 40)],
        format="WebP",
        options={"quality":90},
    )


    objects = UserAccountManager()
    date_joined = models.DateTimeField('date joined', default=timezone.now)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['phone_number']

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def get_phone_number(self):
        return self.phone_number
   
#    OK
    def get_user(self):
        return UserAccount.objects.get(id=self.id)

    # Ok
    def get_orders(self):
        return Order.objects.filter(user=self.get_user())
        
    # Ok
    def get_total_shop(self):
        total=0
        orders = self.get_orders()
        for order in orders:
            total += order.get_total_cost()
        return total

    # Ok
    def get_comments_count(self):
        comments =Comment.objects.filter(user=self.get_user()).count()
        return comments
    
    # Ok
    def get_total_products(self):
        total=0
        orders = self.get_orders()
        for order in orders:
            total += order.get_total_products()
        return total

    # Ok
    def get_total_orders(self):
        orders =self.get_orders().count()
        return orders

    def __str__(self):
        return self.username

