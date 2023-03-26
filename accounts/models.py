from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model

#UserModel = get_user_model()

class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        AGENT = "AGENT", "Agent"
        CLIENT = "CLIENT", "Client"

    base_role = Role.ADMIN

    role = models.CharField(max_length=50, choices=Role.choices)
    NID = models.PositiveIntegerField(null=True, blank=True,unique=True, verbose_name="National Identification Number")
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # Validators should be a list
    #profile_image = models.ImageField(null=True, blank=True, upload_to='profiles/',default='profiles/default-profile.png')     

    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)
        else:
            return super().save(*args, **kwargs)
    

class AgentManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=CustomUser.Role.AGENT)

class Agent(CustomUser):
    base_role = CustomUser.Role.AGENT
    agents = AgentManager()
    class Meta:
        proxy = True
    def welcome(self):
        return "Only for agents"

class AgentProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)


@receiver(post_save, sender=Agent)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "AGENT":
        AgentProfile.objects.create(user=instance)



class ClientManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=CustomUser.Role.CLIENT)

class Client(CustomUser):
    base_role = CustomUser.Role.CLIENT
    clients = ClientManager()
    class Meta:
        proxy = True
    def welcome(self):
        return "Only for clients"

class ClientProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)


@receiver(post_save, sender=Client)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "CLIENT":
        ClientProfile.objects.create(user=instance)

