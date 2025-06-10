from django.contrib import admin

# Register your models here.
from aboutus.models import Caboutus
class homeAdmin(admin.ModelAdmin):
    list_display = ('para_num','aboutus_desc')
admin.site.register(Caboutus, homeAdmin)