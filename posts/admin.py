from django.contrib import admin
from.models import Post,Category,Rating
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display=['headline']

admin.site.register(Post,PostAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display=['category_name']

admin.site.register(Category,CategoryAdmin)

class RatingAdmin(admin.ModelAdmin):
    pass

admin.site.register(Rating,RatingAdmin)