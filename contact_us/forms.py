from django import forms
from .models import ContactMessages


class ContactMessagesForm(forms.ModelForm):
    '''
    This sets out how the contact form on the contact us page wil be rendered
    '''
    class Meta:
        '''
        Sets the fields that will be displayed on the contact us form
        '''
        model = ContactMessages
        fields = ('subject', 'message', 'contact_email')

    def __init__(self, *args, **kwargs):
        '''
        Placeholders to be added to the contact form
        '''
        super().__init__(*args, **kwargs)
        placeholders = {
            'subject': 'Message subject',
            'message': 'Your message',
            'contact_email': 'Your email address',
            }

        # Set all fields as required
        for field in self.fields.values():
            field.required = True

        # Loop through fields to set placeholders and labels
        for field_name, field in self.fields.items():
            # Add asterisk to required fields
            placeholder = f'{placeholders[field_name]} *'
            # Set placeholders
            field.widget.attrs['placeholder'] = placeholder
            # Labels set to false as they are not being used
            field.label = False
