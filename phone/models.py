from django.db import models

class Document(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=500)
    price = models.IntegerField()
    release_date = models.DateField()
    lte_exists = models.BooleanField(default=False)

    slug = models.SlugField(max_length = 200)
# Create your models here.
