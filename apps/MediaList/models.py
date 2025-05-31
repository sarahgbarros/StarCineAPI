from django.db import models

class MediaCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Media Category'

class MediaProduction(models.Model):
    actor = models.JSONField(max_length=255, blank=True, null=True)
    director = models.CharField(max_length=255)
    studio = models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.director},{self.actor}'

    class Meta:
        verbose_name = 'Media Production'

class Media(models.Model):
    title = models.CharField(max_length=255, unique=True)
    synopsis = models.TextField()
    release_date = models.DateField()
    category = models.ForeignKey(MediaCategory, on_delete=models.PROTECT)
    production = models.ForeignKey(MediaProduction, on_delete=models.PROTECT)
    classification = models.CharField(max_length=50, choices= [
        ('L', 'Livre para todos os públicos'),
        ('10', 'Não recomendado para menores de 10 anos'),
        ('12', 'Não recomendado para menores de 12 anos'),
        ('14', 'Não recomendado para menores de 14 anos'),
        ('16', 'Não recomendado para menores de 16 anos'),
        ('18', 'Não recomendado para menores de 18 anos'),
    ])
    duration = models.CharField(max_length=50)
    genres = models.CharField(max_length=125)
    cover = models.ImageField(upload_to='media_cover/', blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Media'
    
