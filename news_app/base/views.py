from django.shortcuts import render
from django.http import HttpResponse

def newsApp(request):
    return HttpResponse('unbiased news')