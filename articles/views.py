from django.shortcuts import render

# Create your views here.


def articles(request):
    """ A view to return the index page """

    return render(request, 'articles/articles.html')