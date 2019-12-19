from django.db import models

# Create your models here.
class Instance(models.Model):
    #ENVS=(('1',u'生产'),('2',u'测试'))

    db_name=models.CharField(max_length=30)
    db_ip=models.GenericIPAddressField()
    db_port=models.IntegerField()
    account=models.CharField(max_length=30)
    env=models.CharField(max_length=2)
    remark=models.CharField(max_length=255,blank=True)
    password=models.CharField(max_length=255)
    
    class Meta:
        unique_together = ('db_name','env',)
