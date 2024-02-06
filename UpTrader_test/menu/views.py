from django.shortcuts import render


def index(request, id=''):
    context = {}
    return render(request, 'menu/index.html', context)
