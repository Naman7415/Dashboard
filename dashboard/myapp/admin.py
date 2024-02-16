from django.contrib import admin
from myapp.models import Bord,Usermodel

# Register your models here.
#admin.site.register(Bord)
admin.site.register(Usermodel)
#eadmin.site.register(Proritymodel)

class BordAdmin(admin.ModelAdmin):
    search_fields = ('priority',)
    list_display = ['title','description']
    
admin.site.register(Bord,BordAdmin)