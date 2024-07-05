from django.db import models

from apps.common.models import BaseModel

# Create your models here.

class Contact(BaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"{self.name}-{self.email}"


class Subscribe(BaseModel):
    email = models.EmailField()

    def __str__(self):
        return self.email
    