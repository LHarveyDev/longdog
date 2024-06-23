from django.db import models


class ContactMessages(models.Model):
    '''
    Contact form model.
    '''
    subject = models.CharField(max_length=80, null=False, blank=False)
    message = models.TextField(max_length=3000, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True, editable=False)
    contact_email = models.EmailField(max_length=254, null=True, blank=True)

    class Meta:
        '''
        To correct the verbose spelling in the Django admin
        '''
        verbose_name_plural = 'Contact Messages'

    def __str__(self):
        '''
        Renames the instance of the model with the subject of the message
        '''
        return self.subject
