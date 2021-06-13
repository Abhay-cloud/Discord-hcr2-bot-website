from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from commands.models import Command

# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def staff(request):
    return render(request, 'home/staff.html')

def terms(request):
    return render(request, 'home/terms.html')

def search(request):
    query = request.GET['query']
    command = Command.objects.all()

    if len(query)>100:
        command = Command.objects.none()
    else:
        command = Command.objects.filter(name__icontains=query)

    params = {'query':query, 'commands':command}
    return render(request, 'home/search.html',params)