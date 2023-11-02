from django.contrib import admin
from mysite.models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=('title','slug','author','date','img')

admin.site.register(Post,PostAdmin)