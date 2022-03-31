from django.db import models

# Create your models here.
class Review(models.Model):
    RATING_CHOICES = [
        (1, '*'),
        (2, '**'),
        (3, '***'),
        (4, '****'),
        (5, '*****')
    ]
    rating = models.IntegerField(choices=RATING_CHOICES)
    text = models.TextField()
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)