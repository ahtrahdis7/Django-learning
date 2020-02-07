from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<em>My Second Project</em>')

def helpp(request):
    helpdict = {'help_insert' : 'HELP PAGE'}
    return render(request, 'help.html', context = helpdict)
    