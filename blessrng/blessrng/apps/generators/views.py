from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from random import randint
from generators.models_dir.dto.dto import RandomIntDto
# Create your views here.

def _get_randint_response(request, dto: RandomIntDto):
    template = loader.get_template('generators/index.html')
    context = {'random_int_dto': dto}
    return HttpResponse(template.render(context, request))

def index(request):
    dto = RandomIntDto(None, None, None)
    return _get_randint_response(request, dto)

def generate(request):
    floor = int(request.POST['floor'])
    ceiling = int(request.POST['ceiling'])
    value = randint(floor, ceiling)
    dto = RandomIntDto(floor, ceiling, value)
    return _get_randint_response(request, dto)
