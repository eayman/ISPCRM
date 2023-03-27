from django.db import models
from accounts.models import Client

class Plan(models.Model):
    speeds = {
        (4,4),
        (8,8),
        (16,16),
        (32,32),
    }
    periods = {
        (1,1),
        (3,3),
        (6,6),
        (12,12),
    }
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=250,null=True,blank=True,help_text="enter details")
    speed = models.PositiveSmallIntegerField(choices=speeds)
    duration = models.PositiveSmallIntegerField(choices=periods)
    month_cost = models.PositiveSmallIntegerField()
    is_popular = models.BooleanField(default=False)
    created_at = models.DateField(auto_now=True, editable=False)

    def __str__(self):
        return str(self.name)

    def total_cost(self):
        return (self.duration * self.month_cost)

class Subscription(models.Model):

    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True,blank=True)
    plan = models.OneToOneField(Plan, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now=True)
    
    #def expiry(self):
    #    return self.start_date + timedelta(months=3)
    
    #def remaining_period(self):
    #    current_date = date.today()  
    #    if current_date > self.expiry:
    #        return (current_date - self.expiry).days 
    #    else:
    #        return 0

    def __str__(self):
        return str(self.id) + " " + str(self.client)
