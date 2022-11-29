from django.db import models

class Author(models.Model):
    class Meta:
     verbose_name = 'Author'
     verbose_name_plural = 'Authors'

    id=models.fields.IntegerField(verbose_name='Author ID',primary_key=True)
    author= models.fields.CharField(verbose_name='Author', max_length=50)

    def __str__(self):
        return self.author


class Quote(models.Model):
    class Meta:
     verbose_name = 'Quote'
     verbose_name_plural = 'Quotes'

    id=models.fields.IntegerField(verbose_name='Quote ID',primary_key=True)
    quote = models.fields.CharField(verbose_name='Quote', max_length=250)
    author_id= models.ForeignKey(Author,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.quote


