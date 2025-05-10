from django.db import models
from django.contrib.auth.models import Group ,  Permission  

# Create your models here.
class Subscription(models.Model):
    name = models.CharField(max_length=100)
    groups = models.ManyToManyField(Group)
    permissions = models.ManyToManyField(Permission,limit_choices_to={'content_type__app_label': 'subscriptions', 'codename__in':['basic','pro','advanced','basic_ai']})
    class Meta:
        permissions = [
            ("advanced", "Advanced Perm"), # subscriptions.advanced
            ("pro", "Pro Perm"), # subscriptions.pro
            ("basic", "Basic Perm") ,# subscriptions.basic
            ("basic_ai","Basic AI Perm")
        ]
       
