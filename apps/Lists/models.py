from django.db import models
from apps.MediaList.models import Media
from apps.Users.models import User



class ListCategory(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class List(models.Model):
    category = models.ForeignKey(ListCategory, on_delete=models.PROTECT)
    media = models.ManyToManyField(Media)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
