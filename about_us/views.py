from django.shortcuts import render


def about_us(request):
    '''
    View that returns the about us page
    '''
    return render(request, 'about_us/about_us.html')
