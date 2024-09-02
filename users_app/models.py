from django.db import models

# Create your models here.
class User(models.Model):
    roles = [
        ("admin", 'admin'),
        ("user", "user")
    ]

    name = models.CharField(max_length=15)

    email = models.EmailField()
    role = models.CharField(max_length=5, choices=roles, default="user")