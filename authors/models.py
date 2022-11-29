#Create your models here.
from django.db import models

class Author(models.Model):
    class Meta:
     verbose_name = 'Author'
     verbose_name_plural = 'Authors'

    id=models.fields.IntegerField(verbose_name='Author ID',primary_key=True)
    author= models.fields.CharField(verbose_name='Author', max_length=50)

    def __str__(self):
        return self.author
