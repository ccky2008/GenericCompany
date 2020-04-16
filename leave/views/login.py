from django.http import HttpResponseRedirect
from django.shortcuts import render

def login(request):
    return render(request, 'leave/login.html', {})