from django.shortcuts import render
from commands.models import Command
from django.http import JsonResponse

# Create your views here.
def commands(request):
    commands = Command.objects.all()
    print(commands)
    param = {'commands':commands}
    return render(request, 'commands/commands.html', param)

def api(request):
    command = request.GET.get("command")
    try:
        commands = Command.objects.all().values()
        commands1 = commands.get(name=command)
        return JsonResponse(commands1, safe=False)
    except Command.DoesNotExist:
        return JsonResponse({'error': 'Command Not Found'})
            