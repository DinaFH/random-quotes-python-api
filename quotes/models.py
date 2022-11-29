from django.db import models
from authors.models import Author
class Quote(models.Model):
    class Meta:
     verbose_name = 'Quote'
     verbose_name_plural = 'Quotes'

    id=models.fields.IntegerField(verbose_name='Quote ID',primary_key=True)
    quote = models.fields.CharField(verbose_name='Quote', max_length=250)
    author_id= models.ForeignKey(Author,on_delete=models.CASCADE)

    def __str__(self):
        return self.quote