from django.db import models

# Create your models here.
class School(models.Model):
    sname=models.CharField(max_length=100)
    sid=models.IntegerField(primary_key=True)
    saddress=models.TextField(max_length=100)


    def __str__(self):
        return self.sname
