from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass
    # add additional fields in here
    email    = models.EmailField(unique=True)
    zip_code = models.CharField(max_length=10,null=True)
    mobile_no= models.CharField(max_length=11, null=True)

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['mobile_no']

    def __str__(self):
        return self.email