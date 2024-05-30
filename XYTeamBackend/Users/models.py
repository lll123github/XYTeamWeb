from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=20,blank=True,null=True)
    password = models.CharField(max_length=40)
    email = models.EmailField(blank=True,null=True)
    phone = models.PositiveBigIntegerField(blank=True,null=True)
    TMPID = models.PositiveIntegerField(primary_key=True)
    TMPName = models.CharField(max_length=20,blank=True,null=True)
    steamID = models.PositiveBigIntegerField(blank=True,null=True)
    QQ = models.PositiveBigIntegerField(blank=True,null=True)
