from django.db.models.signals import pre_save, post_save, post_delete
from .models import Product
from django.dispatch import receiver
from .recommendation import export


@receiver(pre_save, sender=Product)
def price_after_dis(sender, instance, **kwargs):
    # instance.old_price = instance.price
    instance.new_price = instance.get_price_after_dis()

@receiver(post_save, sender=Product)
def export_products_save(sender, instance, **kwargs):
    export()

@receiver(post_delete, sender=Product)
def export_products_delete(sender, instance, **kwargs):
    export()





