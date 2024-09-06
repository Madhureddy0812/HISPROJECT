from django.contrib import admin
from .models import *
# Register your models here.

class appreg_admin(admin.ModelAdmin):
    list_display = ['APP_ID','FULLNAME','EMAIL','PHNO','SSN','GENDER','STATE_NAME','CREATE_DATE','UPDATE_DATE','CREATED_BY','UPDATED_BY']


admin.site.register(appReg_Module,appreg_admin)