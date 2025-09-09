from django.db import models
from accounts.models import EditorsProfile
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=200)
    def __str__(self):
        return self.category_name
    
class Post(models.Model):  
    created_at = models.DateTimeField(auto_now_add = True)
    edited_at = models.DateTimeField(auto_now = True)
    categroy = models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,default=None) 
    headline = models.CharField(max_length=200)
    description = models.TextField()
    editor = models.ForeignKey(EditorsProfile,on_delete=models.CASCADE,related_name='my_post') 
    image = models.ImageField(upload_to='photos/post_img')
    viwes_of_this = models.IntegerField(blank=True,default=0)
   
    def rating(self):
       now = 0.0
       ave = now
       qeryset_of_rating = Rating.objects.filter(post=self).exists()
       if qeryset_of_rating:
            qeryset_of_rating = Rating.objects.filter(post=self)
            n = qeryset_of_rating.count()
            for i in qeryset_of_rating:now+=i.rating
            ave = now/n
       return  round(ave, 1)   
    
    
    def short_descriptions(self):
        if len(self.description) > 50:
            return f"{str(self.description)[:50]}..."
        else:
            return f"{str(self.description)}"
        
    def __lt__(self, others): 
        my_rate = self.rating()
        other_rate = others.rating()
        return my_rate <= other_rate
    
       
RATING= (
    (0, '0 out of 4'),
    (1, '1 out of 4'),
    (2, '2 out of 4'),
    (3, '3 out of 4'),
    (4, '4 out of 4'),
    
)

class Rating(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='ratins')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='ratins')
    descriptions = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    edited_at = models.DateTimeField(auto_now = True)
    rating = models.IntegerField(choices=RATING) 

    class Meta:
        unique_together = (('post', 'user'),)
  