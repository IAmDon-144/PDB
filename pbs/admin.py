from django.contrib import admin
from .models import PBS, Zonal, SubZonal, ComplainCenter, Fider, Report

# Register your models here.


@admin.register(PBS)
class PBS(admin.ModelAdmin):
    list_display = ['id', 'name', 'type']



@admin.register(Zonal)
class Zonal(admin.ModelAdmin):
    list_display = ['id', 'name', 'type']


@admin.register(SubZonal)
class SubZonal(admin.ModelAdmin):
    list_display = ['id', 'name', 'type']


@admin.register(ComplainCenter)
class ComplainCenter(admin.ModelAdmin):
    list_display = ['id', 'name', 'type']


@admin.register(Fider)
class Fider(admin.ModelAdmin):
    list_display = ['id', 'name', 'type', "fiderNo",
                    "latitude", "longitude", "status",]
    search_fields = ("name", )



admin.site.site_header = "PDB Administration"
admin.site.site_title = "PDB Admin Portal"
admin.site.index_title = "Welcome to Admin Site"
