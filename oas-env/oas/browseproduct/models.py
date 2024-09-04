from django.db import models


class cards(models.Model):
    title = models.CharField(max_length=60)
    text = models.TextField()
    price = models.IntegerField()
    image = models.FileField(upload_to="browseproduct/",null=True)
    category = models.CharField(max_length=60)


# Create your models here.
