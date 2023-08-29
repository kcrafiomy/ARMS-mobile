
# Create your models here.
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Mobile(models.Model):
    CONDITION_CHOICES = (
        ('A grade', 'Excellent'),
        ('good', 'Good'),
        ('fair', 'Fair'),
    )

    STORAGE_CHOICES = (
        ('16', '16 GB'),
        ('32', '32 GB'),
        ('64', '64 GB'),
        ('128', '128 GB'),
        ('256', '256 GB'),
        ('512', '512 GB'),
        ('1 tb', '1 TB'),
    )

    brand = models.CharField(max_length=50)
    model_name = models.CharField(max_length=100)
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES)
    storage_capacity = models.CharField(max_length=10, choices=STORAGE_CHOICES)
    color = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='mobile_images/', default='default_image.jpg')
    image_1 = models.ImageField(upload_to='mobile_images/', default='default_image.jpg')
    image_2 = models.ImageField(upload_to='mobile_images/', default='default_image.jpg')
    posted_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category)  # Adding the many-to-many relationship
    description = models.TextField(default='No description available')
    
    def __str__(self):
        return f"{self.brand} {self.model_name} - {self.storage_capacity}"

    class Meta:
        ordering = ['-posted_at']


