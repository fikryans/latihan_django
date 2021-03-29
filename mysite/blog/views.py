from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    first_name = 'Fikri'
    last_name = 'Aja'

    context = {
        'first_name':first_name,
        'last_name':last_name,
    }
    return render(request, "index.html", context)

