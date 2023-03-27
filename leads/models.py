from django.db import models
from django.core.validators import RegexValidator

class Lead(models.Model):
    provinces = [
    ('Gaza', 'Gaza'),
    ('North Gaza', 'North Gaza'),
    ('Central', 'Central'),
    ('Khan Yunis', ' Khan Yunis'),
    ('Rafah', 'Rafah'),
    ]
    first_name = models.CharField(max_length=200, null=False, blank=False)
    last_name = models.CharField(max_length=200, null=False, blank=False)
    address = models.CharField(max_length=50,choices=provinces, null=True, blank=True)
    email = models.EmailField(null=True, blank=True,unique=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17) # Validators should be a list
    fb_account = models.URLField( null=True, blank=True)
    is_contacted = models.BooleanField(default=False)
    #agent = models.ForeignKey(Agent, null=True, blank=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.first_name + " " + self.last_name