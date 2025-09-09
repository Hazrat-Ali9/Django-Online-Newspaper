from django.contrib.auth.models import User
from django import forms
from . models import Post,Rating   
    
class PostCrationsForm(forms.ModelForm):
    class Meta:
         model=Post
         fields = ['categroy', 'headline','description', 'image']

class RatingForm(forms.ModelForm):
    class Meta:
        model= Rating
        fields = ['rating', 'descriptions']
         