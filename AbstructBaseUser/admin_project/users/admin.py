from django.contrib import admin
#from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.

# class AccountAdmin(UserAdmin):
# 	list_display = ()
# 	ordering = ()
# 	filter_horizontal = ()
# 	list_filter = ()
# 	fieldsets = ()

admin.site.register(CustomUser)
