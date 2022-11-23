from django.contrib import admin
from .models import ApiUser,Post, Reply

# Register your models here.

admin.site.register(ApiUser)
admin.site.register(Post)
admin.site.register(Reply)
