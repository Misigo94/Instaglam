
from re import I
from django.db import models

# Create your models here.

 
class Image(models.Model):
   image = models.ImageField(upload_to='pic/%y/',blank=True)
   img_name = models.CharField(max_length=200, blank=True)
   imge_caption = models.CharField(max_length=200,blank=True)
   date_posted = models.DateTimeField(auto_now_add=True,blank=True)
   
   def __str__(self):
       return self.img_name

class Profile(models.Model):
   name = models.CharField(max_length=200, blank=True)
   username = models.CharField(max_length=200, blank=True)
   profile_photo = models.ImageField(upload_to='pic/%y/',blank=True)
   image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)
   bio = models.TextField(max_length=200,blank=True)
 
   def __str__(self):
       return self.name

@classmethod
def search_by_username(cls,search_username):
        username = Profile.objects.filter(profile__username__icontains=search_username)
        return username

   
class Comments(models.Model):
   comment = models.TextField(max_length=200,null=True, blank=True)
   image = models.ForeignKey(Image,on_delete=models.CASCADE,null=True,blank=True)
   author = models.ForeignKey(Profile,on_delete=models.CASCADE, blank=True)
 
   def __str__(self):
       return self.comment

class Likes(models.Model):
    user = models.ForeignKey(Profile, related_name='likes', on_delete=models.CASCADE)
    image = models.ForeignKey(Image, related_name='likes', on_delete=models.CASCADE)

class Login(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=20)

# Create your models here.
