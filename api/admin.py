from django.contrib import admin
from .models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','name','type','active','added_date')

admin.site.register(User,UserAdmin)
