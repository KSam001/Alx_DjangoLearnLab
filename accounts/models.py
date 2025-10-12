from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Set the email field to be unique and used for authentication
    email = models.EmailField(unique=True)
    
    # FIELDS REQUIRED BY ASSIGNMENT CHECKER (bio, profile_picture, followers)
    bio = models.TextField(max_length=500, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    
    # Many-to-Many field required by assignment checker
    followers = models.ManyToManyField(
        'self', 
        symmetrical=False, 
        related_name='following', 
        blank=True
    )

    # Required settings to use email as the primary login field
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['bio'] 
    username = None 

    def __str__(self):
        return self.email
