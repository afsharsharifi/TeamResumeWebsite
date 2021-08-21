from BackPyContactUs.models import ContactUs
from django.contrib import admin

# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'full_name', 'is_read']
    list_filter = ['is_read']
    list_editable = ['is_read']
    search_fields = ['full_name', 'subject']

    class Meta:
        model = ContactUs


admin.site.register(ContactUs, ContactAdmin)