from django.db import models

# Create your models here.


class Command(models.Model):
    sno = models.AutoField(primary_key=True)
    category = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    ShortDescription = models.TextField()
    LongDescription = models.TextField()
    permissions = models.CharField(max_length=255)


    

    def __str__(self):
        return self.category + ":" + self.name