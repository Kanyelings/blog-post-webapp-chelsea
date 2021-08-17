from django.db import models


# Create your models here.
class RecipePost(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='static/uploads/images', default='')
    description = models.TextField(max_length=200, default=' ')
    ingredients = models.CharField(max_length=50)
    instructions = models.TextField(max_length=500)

    def __str__(self):
        return self.name
