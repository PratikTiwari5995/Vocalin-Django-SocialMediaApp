from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, email=instance.email)



@receiver(post_save, sender=Profile)
def update_user_email_from_profile(sender, instance, created, **kwargs):
    if not created:
        user = instance.user
        if user.email != instance.email:
            user.email = instance.email
            user.save()
