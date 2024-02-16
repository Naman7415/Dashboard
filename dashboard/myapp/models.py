from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.







    
class Usermodel(AbstractUser):
   username = models.CharField(max_length = 50 , unique = True,blank=True,null=True)
   password=models.CharField(max_length=100)
   
   
   
class Bord(models.Model):
    user=models.ForeignKey(Usermodel,on_delete=models.CASCADE,related_name='bords')
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    duedate = models.DateTimeField(auto_created = True)
    list=(('High','High'),('Medium','Medium'),('Low','Low'))
    priority= models.CharField(max_length=50,choices=list)
    
    
    def __str__(self):
        return self.description
    
#    REQUIRED_FIELDS = [ 'password']
    # username=models.CharField(max_length=100,unique=True)
    # password=models.IntegerField()
    
    # REQUIRED_FIELDS = [username,password]
    
    # # def __str__(self):
    # #     return self.username
    
# class Proritymodel(models.Model):
#    li=(('High','High'),('Medium','Medium'),('Low','Low'))
#    prorityfield=models.CharField(max_length=100 , choices=li)
   
#    def __str__(self):
#       return self.prorityfield