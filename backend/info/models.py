from django.db import models


class CardModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name
