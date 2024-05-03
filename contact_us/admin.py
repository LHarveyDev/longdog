from django.contrib import admin
from .models import ContactMessages


class ContactMessagesAdmin(admin.ModelAdmin):
    '''
    Displays the fields that will be displayed in the Django admin page
    '''
    list_display = (
      'subject',
      'date',
      'contact_email',
    )
    # Sets the ordering of the items in the django admin page.
    # Currently set to be organized by date
    ordering = ('date',)


admin.site.register(ContactMessages, ContactMessagesAdmin)
