from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def index(request):
    p = Players.objects.all()

    context = {'players': p}
    return render(request, 'crud/base.html', context)



def add(request):
    if request.method=='POST':
        name = request.POST.get('name')
        category = request.POST.get('category')
        team = request.POST.get('team')
        country = request.POST.get('country')

        p = Players(
            name = name,
            category = category,
            team = team,
            country = country
        )
        p.save()
        return redirect('home')

    return render(request, 'crud/base.html')



def update(request, id):
    if request.method=='POST':
        name = request.POST.get('name')
        category = request.POST.get('category')
        team = request.POST.get('team')
        country = request.POST.get('country')

        p = Players(
            id = id,
            name = name,
            category = category,
            team = team,
            country = country
        )
        p.save()
        return redirect('home')
    return render(request, 'crud/base.html')



def delete(request, id):
    p = Players.objects.filter(id=id)
    p.delete()
    return redirect('home')


def deletePlayers(request):
    p = Players.objects.all().delete()
    return redirect('home')