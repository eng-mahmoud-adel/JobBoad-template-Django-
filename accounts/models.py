from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    city = models.ForeignKey("City", null=True, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=50)
    image = models.ImageField(upload_to='profiles/images')
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.user)
    

# create a profile once a user has registered an account using signals
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

class City(models.Model):
    name = models.CharField(max_length=50, default='Cairo')

    def __str__(self):
        return self.name
    