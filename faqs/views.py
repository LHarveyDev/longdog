from django.shortcuts import render


def faqs(request):
    """ A view to return the faqs page """

    return render(request, 'faqs/faqs.html')
