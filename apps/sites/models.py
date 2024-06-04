from django.db import models


# Create your models here.

class Site(models.Model):
    site_name = models.CharField(max_length=100,blank=False,null=False)
    base_url       = models.URLField()
    redirect_url = models.URLField()
    token       = models.CharField(max_length=1000,blank=False,null=False)
    
    
    def __str__(self) -> str:
        return self.site_name