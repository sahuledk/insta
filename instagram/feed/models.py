from django.db import models
import uuid
from user.models import Profile

# Create your models here.


class Feed(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    photo = models.ImageField(null=True, blank=True)
    status = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['-created']

