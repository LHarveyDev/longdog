from django.db import models
from profiles.models import UserProfile
from products.models import Product


class ProductReview(models.Model):
    '''
    The review model which allows users to review a product
    '''
    review_title = models.CharField(max_length=90, null=False, blank=False)
    reviewed_product = models.ForeignKey(Product, null=False, blank=False,
                                         on_delete=models.CASCADE,)
    reviewer = models.ForeignKey(UserProfile, null=False, blank=False,
                                 on_delete=models.CASCADE)
    review = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        '''
        This will correct the verbose spelling in Django admin to the correct\
        plural spelling of reviews
        '''
        verbose_name_plural = 'Reviews'

    def __str__(self):
        '''
        Renames the instance of the ProductReview model with the review title
        '''
        return self.review_title
