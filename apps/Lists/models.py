from django.db import models



class ListCategory(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class List(models.Model):
    category = models.ForeignKey(ListCategory, on_delete=models.PROTECT)
    media = models.ForeignKey('MediaList.Media', on_delete=models.PROTECT)
    user = models.ForeignKey('Users.User', on_delete=models.PROTECT)
