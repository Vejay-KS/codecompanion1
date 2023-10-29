from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
#from django.contrib.auth import get_user_model
from .models import CodeCompanionUser

class CodeCompanionUserAdmin(BaseUserAdmin):
    #fieldsets = ((None, {'fields': ('email', 'password', )}))
    add_fieldsets = (
      (None, {
          'classes': ('wide', ),
          'fields': ('username', 'password1', 'password2'),
      }),
  )
    #'password1', 'password2', 
    list_display = ('username', 'firstname', 'lastname', 'email')

# Register your models here.

admin.site.register(CodeCompanionUser, CodeCompanionUserAdmin)

# password1=models.CharField(max_length=200)
#     password2=models.CharField(max_length=200)