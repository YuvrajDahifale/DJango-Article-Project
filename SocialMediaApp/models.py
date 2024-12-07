from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=100)
    slug=models.CharField(max_length=100,null=True,blank=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    likes=models.ManyToManyField(User,related_name='likes',null=True)
    created_date=models.DateField()
    body=models.CharField(max_length=5000)

    def __str__(self):
        return self.title
    
    def absolute_url(self):
        return reverse('article_used',args=[self.id,self.slug])
    





    
@receiver(pre_save,sender=Article)
def pre_save_slug(sender,**kwargs):
    slug1=slugify(kwargs['instance'].title)
    kwargs['instance'].slug=slug1
