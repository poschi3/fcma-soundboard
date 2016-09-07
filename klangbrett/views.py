from django.shortcuts import render

from .models import Klang

def index(request):
    klang_list = Klang.objects.all()
    context = {'klang_list': klang_list}
    return render(request, 'klangbrett/index.html', context)