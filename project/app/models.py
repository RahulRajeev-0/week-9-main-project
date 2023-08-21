from django.db import models

# Create your models here.
class User_details(models.Model):
    name=models.CharField(max_length=25,blank=False,null=False,unique=True)
    email=models.EmailField()
    password=models.CharField(max_length=25,blank=False,null=False)
    #confirm_password=models.CharField(max_length=25,blank=False,null=False)

    def __str__(self):
        return self.name