from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def footer(request):
    return render(request, 'footer.html')

def space(request, pk):
    msg = 'Message'
    if pk == '0':
        return render(request, 'spaces/allspaces.html')
    else:
        return render(request, 'spaces/space.html', {'message':msg})