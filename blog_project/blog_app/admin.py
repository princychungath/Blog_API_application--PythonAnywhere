from django.contrib import admin
from .models import User,Post

class User_admin(admin.ModelAdmin):
    list_display = ['username'] 
admin.site.register(User,User_admin)

admin.site.register(Post)