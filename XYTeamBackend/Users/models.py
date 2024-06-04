from django.db import models

# Create your models here.

class UserInfo(models.Model):
    user =models.OneToOneField('auth.User',on_delete=models.CASCADE)
    phone = models.PositiveBigIntegerField(blank=True,null=True)
    TMPID = models.PositiveIntegerField(primary_key=True)
    TMPName = models.CharField(max_length=20,blank=True,null=True)
    steamID = models.PositiveBigIntegerField(blank=True,null=True)
    QQ = models.PositiveBigIntegerField(blank=True,null=True)
