from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest
from .models import ApplicationsForEditors,EditorsProfile,Editors

# Register your models here.

class ApplicationsForEditorsAdmin(admin.ModelAdmin):
    list_display=['user','aproved']

    def save_model(self, request, obj, form, change):  
        if form.cleaned_data['aproved']:
            user = obj.user
            EditorsProfile.objects.create(
               user=user,
               first_name=obj.first_name,
               last_name=obj.last_name,
               phone_number=obj.phone_number,
               n_id=obj.n_id,
               gender=obj.gender,
               educations=obj.educations,
               state=obj.state,
               city=obj.city,
               zip_code=obj.zip_code,
               country=obj. country,
            )
            Editors.objects.create(user_name=user.username)
        super().save_model(request, obj, form, change)
        
admin.site.register(ApplicationsForEditors,ApplicationsForEditorsAdmin)

class EditorsProfileAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','is_active']
admin.site.register(EditorsProfile,EditorsProfileAdmin)

class EditorsAdmin(admin.ModelAdmin):
    list_display=['user_name']
admin.site.register(Editors,EditorsAdmin)