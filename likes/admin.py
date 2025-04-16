from django.contrib import admin
from .models import Like  # make sure the Like model is correctly imported

admin.site.register(Like)