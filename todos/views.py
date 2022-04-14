from django.shortcuts import render
from .models import Todo

def index(request):
    elements = Todo.objects.all()

    context = {'elements': elements}

    return render(request, 'index.html', context)
