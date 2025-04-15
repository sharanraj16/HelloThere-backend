from django.contrib import admin
from .models import Post  # make sure the model is imported

admin.site.register(Post)  # this makes it show up
