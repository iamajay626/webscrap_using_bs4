from django.db import models

# Create your models here.
class links(models.Model):
    def __str__(self):
        if self.string_name:
            return self.string_name
        else:
            return "unnamed link"

    address=models.CharField(max_length=500,null=True,blank=True)
    string_name=models.CharField(max_length=500,null=True,blank=True)

