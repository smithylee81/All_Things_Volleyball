from django.shortcuts import render

# Create your views here.
""" Views has been copied and
    adapted from the CI's Boutique Ado project """

def index(request):
    """ View to return the index page """

    return render(request, 'home/index.html')