from django.db import models
from apps.Users.models import User
from apps.MediaList.models import Media

class Review(models.Model):
    rate = models.IntegerField()
    comment = models.CharField(max_length=300)
    user = models.ForeignKey('Users.User', on_delete=models.PROTECT)
    media = models.ForeignKey(Media, on_delete=models.PROTECT)

    class Meta:
        unique_together = ['user', 'media', 'rate']