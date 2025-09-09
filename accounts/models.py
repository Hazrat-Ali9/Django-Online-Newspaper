from django.db import models
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

GENDER = (
    (1, 'MALE'),
    (2, 'FEMALE'),
    (3, 'OTHERS'),
)

class ApplicationsForEditors(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=17)
    n_id = models.CharField(max_length=17)
    gender = models.IntegerField(choices=GENDER) 
    email = models.EmailField()
    educations = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=6)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    applicatoins_date = models.DateTimeField(auto_now=True)
    aproved = models.BooleanField(default=False)

    class Meta:
        ordering = ['applicatoins_date']

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class EditorsProfile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='editor_profile')
    phone_number = models.CharField(max_length=17)
    n_id = models.CharField(max_length=17)
    gender = models.IntegerField(choices=GENDER)  
    educations = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=6)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    ragistraions_date = models.DateTimeField(auto_now_add=True)
    profile_update_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    tota_posts = models.IntegerField(default=0)

    def total_views_coutnt_for_thid_editor(self):
        all_Post = self.my_post.all()
        now = 0
        for i in all_Post:now+=i.viwes_of_this
        return now
    
    def ave_rating(self):
        all_Post = self.my_post.all()
        n =  all_Post.count()
        now = 0
        for i in all_Post:now+=i.rating()
        if now>0:
           ave = now/n
           return  round(ave, 1) 
        else :return 0.0

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Editors(models.Model):
    user_name = models.CharField(max_length=50)