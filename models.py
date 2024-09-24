from django.db import models # type: ignore
from django.contrib.auth.models import User # type: ignore
# Create your models here.

class Recipe(models.Model):
    
    recipe_name=models.CharField(max_length=100)
    recipe_description=models.TextField()
    recipe_image=models.ImageField(upload_to="recipe")
    recipe_view_count=models.IntegerField(default=1)
