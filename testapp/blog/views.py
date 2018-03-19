from django.http import HttpResponse
from django.shortcuts import render
from random import randint

def index(request):
#    random_number = randint(1,10)
#    return HttpResponse("Hello, world. You're at the polls index.{}".format(random_number))
# Create your views here.
    name = 'junho'
    return render(request, "index.html", {'name' : name})
