from django.contrib import admin
from .models import ContactUs
# Register your models here.
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'is_read_by_admin')


admin.site.register(ContactUs, ContactUsAdmin)