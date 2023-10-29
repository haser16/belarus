from django.contrib import admin

from main.models import (IT, Agriculture, Architecture, CarBuilding,
                         Construction, Culture, Forestry, Industry, Medicine)

admin.site.register(Medicine)
admin.site.register(Industry)
admin.site.register(Construction)
admin.site.register(CarBuilding)
admin.site.register(Agriculture)
admin.site.register(Forestry)
admin.site.register(IT)
admin.site.register(Architecture)
admin.site.register(Culture)
