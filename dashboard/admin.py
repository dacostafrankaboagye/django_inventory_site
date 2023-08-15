from django.contrib import admin
from .models import Product, Order

#from django.contrib.auth.models import Groups


# change the header
admin.site.site_header = 'Main Admin Dashboard'

class ProductAdmin(admin.ModelAdmin):
	list_display = ('name','category', 'quantity',)
	list_filter = ('quantity', )
	# or like this list_filter = ['quantity']




# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)

# unregister
#admin.site.unregister(Group)


