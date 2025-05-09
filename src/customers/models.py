from django.db import models
from django.conf import settings
import helpers.billing
# Create your models here.
User  =settings.AUTH_USER_MODEL
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    stripe_id = models.CharField(max_length=20,null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.username}"
    
       #def save(self, *args, **kwargs):
        #self.stripe_id= "fdbhin"
        #stripe_response = helpers.billing.create_customer(raw=True)
        #super().save(*args, **kwargs)"""

    def save (self, *args, **kwargs):
        if not self.stripe_id:
            email = self.user.email
            if email != "" or email is not None:
                stripe_id= helpers.billing.create_customer(email=email, raw=False)
                self.stripe_id= stripe_id
        super().save(*args, **kwargs)