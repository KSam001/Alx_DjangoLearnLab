from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Set the email field to be unique and used for authentication
    email = models.EmailField(unique=True)
    
    # Custom fields from the plan
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    # Required settings to use email as the primary login field
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']
    username = None 

    def __str__(self):
        return self.email
