from django.db import models

# Create your models here.
class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255,null=True)
    email=models.CharField(max_length=100,null=True)
    phone=models.CharField(max_length=13,null=True)
    content=models.TextField(null=True)
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    def __str__(self):
        return "Details about "+ self.name