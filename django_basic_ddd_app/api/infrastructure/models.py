from django.db import models
import uuid


class ProductModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    num_reviews = models.IntegerField()
    average_rating = models.FloatField(null=True)


class ReviewModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.CharField(max_length=255)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    rating = models.IntegerField()
    description = models.TextField()
