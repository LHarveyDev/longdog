from django.shortcuts import render

# Create your views here.


def faqs(request):
    """ A view to return the index page """

    return render(request, 'faqs/faqs.html')