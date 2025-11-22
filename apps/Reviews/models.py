from django.db import models
from apps.Users.models import User
from apps.MediaList.models import Media

class Review(models.Model):
    rate = models.IntegerField()
    comment = models.CharField(max_length=300)
    user = models.ForeignKey('Users.User', on_delete=models.PROTECT)
    media = models.ForeignKey(Media, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    likes = models.IntegerField(default=0, null=True)

    class Meta:
        unique_together = ['user', 'media', 'rate']