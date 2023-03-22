from django.contrib import admin
from amazon.models import Amazon
# Register your models here.


class AmazonAdmin(admin.ModelAdmin):
    list_display = ['name', 'price' , 'quantity' ]
    search_fields = ['name']


admin.site.register(Amazon, AmazonAdmin)