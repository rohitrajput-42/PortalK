from django.contrib import admin
from .models.product import Product
from .models.customer import Customer
from .models.joblist import Joblist

from .models.skillcat import Skillcat
from .models.ecat import Ecat
from .models.lcat import Lcat
from .models.icat import Icat
from .models.scat import Scat

class AdminProduct(admin.ModelAdmin):    
    list_display = ['name', 'description', 'eligibilty']

class AdminSkillcat(admin.ModelAdmin):
    list_display = ['name']

class AdminEcat(admin.ModelAdmin):
    list_display = ['name']

class AdminLcat(admin.ModelAdmin):
    list_display = ['name']

class AdminIcat(admin.ModelAdmin):
    list_display = ['name']

class AdminScat(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Product, AdminProduct)
admin.site.register(Customer)
admin.site.register(Joblist)

admin.site.register(Skillcat, AdminSkillcat)
admin.site.register(Ecat, AdminEcat)
admin.site.register(Lcat, AdminLcat)
admin.site.register(Icat, AdminIcat)
admin.site.register(Scat, AdminScat)