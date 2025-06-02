from django.contrib import admin
from .models import User, Blog, Comment
# Register your models here.
admin.site.register([
    User,
    Blog,
    Comment
])