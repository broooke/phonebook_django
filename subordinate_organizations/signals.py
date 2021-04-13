from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Customer, Subdepartment, Department

@receiver(post_save, sender=Subdepartment)
def delete_users(sender, instance, created, **kwargs):
    for user in Customer.objects.all():
        if user.subdepartment is None:
            user.delete()

@receiver(post_save, sender=Customer)
def delete_users_1(sender, instance, created, **kwargs):
    for user in Customer.objects.all():
        if user.subdepartment is None:
            user.delete()

@receiver(post_delete, sender=Subdepartment)
def delete_users_2(sender, instance, **kwargs):
    for user in Customer.objects.all():
        if user.subdepartment is None:
            user.delete()

