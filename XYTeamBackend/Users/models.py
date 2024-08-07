from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.

class UserInfo(models.Model):
    user =models.OneToOneField('auth.User',on_delete=models.CASCADE)
    phone = models.PositiveBigIntegerField(blank=True,null=True,validators=[MinValueValidator(10000000000),MaxValueValidator(99999999999)])
    TMPID = models.PositiveIntegerField(primary_key=True,validators=[MaxValueValidator(9999999)])
    TMPName = models.CharField(max_length=20,blank=True,null=True)
    steamID = models.PositiveBigIntegerField(blank=True,null=True,validators=[MinValueValidator(10000000000000000),MaxValueValidator(99999999999999999)])
    QQ = models.PositiveBigIntegerField(blank=True,null=True)
    credit = models.PositiveBigIntegerField(default=0)
