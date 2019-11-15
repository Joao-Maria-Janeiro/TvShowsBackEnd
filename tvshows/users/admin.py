from django.contrib import admin
from .models import TvShow, UserProfile, Suggestion

# Register your models here.
admin.site.register(TvShow)
admin.site.register(UserProfile)
admin.site.register(Suggestion)