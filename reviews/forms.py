from django import forms
from django.forms import HiddenInput
from .models import ProductReview


class ProductReviewForm(forms.ModelForm):
    '''
    This details how the product review form will display
    '''
    class Meta:
        '''
        The fields on the form that will be displayed. Reviewer is hidden
        '''
        model = ProductReview
        fields = ('review_title', 'reviewed_product', 'reviewer', 'review')
        widgets = {'reviewer': HiddenInput()}

    def __init__(self, *args, **kwargs):
        '''
        Placeholders to be added to the reviewed product fields
        '''
        super().__init__(*args, **kwargs)
        placeholders = {
            'review_title': 'Review Title',
            'reviewed_product': 'Reviewed Product',
            'reviewer': 'Reviewed By',
            'review': 'Your Review',
            }

        # Form will auto start on review title
        self.fields['review_title'].widget.attrs['autofocus'] = True
        for field in self.fields:
            # Asterisk will appear on required fields
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            # Set placeholders
            self.fields[field].widget.attrs['placeholder'] = placeholder
            # Labels set to false as they are not being used
            self.fields[field].label = False
