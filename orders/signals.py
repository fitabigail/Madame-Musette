from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import OrderProduct

# Copied from ButiqueAdo and addapted for MadaMusette


@receiver(post_save, sender=OrderProduct)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on orderitem update/create
    """
    instance.order.update_total()
 

@receiver(post_delete, sender=OrderProduct)
def update_on_save(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
    """
    instance.order.update_total()
