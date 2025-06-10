from django.contrib import admin
from home.models import home
class homeAdmin(admin.ModelAdmin):
    list_display = ('para_num','home_desc','home_img')
admin.site.register(home, homeAdmin)
