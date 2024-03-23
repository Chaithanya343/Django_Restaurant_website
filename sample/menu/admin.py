from django.contrib import admin
from menu.models import menu
# Register your models here.
class menuAdmin(admin.ModelAdmin):
    list_disp=['menu_icom','menu_title','menu_des']
admin.site.register(menu,menuAdmin)