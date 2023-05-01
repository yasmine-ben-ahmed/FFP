from django.contrib import admin
from django.contrib.gis import admin
from .models import node
from .models import myProject
from .models import Data
from .models import parcelle
admin.site.register(parcelle)


admin.site.register(Data)


admin.site.register(node)
admin.site.register(myProject)
class polygonAdmin(admin.GISModelAdmin):
    list_display = ("geom")

class myProjectAdmin(admin.ModelAdmin):
    list_display = ['polygon_id', 'nomp', 'descp', 'debutp', 'finp', 'cityp', 'clientp']