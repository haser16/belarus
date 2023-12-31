from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=126)

    def __str__(self):
        return f'{self.name}'


class Content(models.Model):
    image = models.ImageField(upload_to='image_content')
    category = models.ForeignKey(to=Category, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.category}'


class Paragraphs(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='paragraphs')
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name='paragraphs')

    def __str__(self):
        return f'{self.content}'

