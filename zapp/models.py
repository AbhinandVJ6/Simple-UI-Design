from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Api(models.Model):
    class Meta():
        db_table = 'api'

    topic = models.CharField(
        max_length=200, db_index=True, null=False, blank=False
    )

    image = CloudinaryField(
        'Image', blank=False, db_index=True, null=False
    )

    name = models.CharField(
        'Name', max_length=40, db_index=True,null=False,blank=False
    )
    
    duration = models.IntegerField(
         db_index=True
    )

    date = models.DateField(
        db_index=True, null=False, blank=False
    )

    time_one = models.TimeField(
        db_index=True, auto_now=False
    )

    time_two = models.TimeField(
        db_index=True, auto_now=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name
    
