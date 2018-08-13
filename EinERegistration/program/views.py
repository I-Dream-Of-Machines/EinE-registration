from django.shortcuts import HttpResponse
from django.template import loader
from .models import Program
from .models import ProgramLevel
from .models import Iteration

# Create your views here.


def index(request):
    program_list = Program.objects.all()
    template = loader.get_template('program/index.html')
    context = {'program_list': program_list,
               }
    return HttpResponse(template.render(context, request))


def levels(request, program_title):
    program_list = Program.objects.filter(name=program_title)
    level_list = ProgramLevel.objects.filter(category=program_list[0])
    template = loader.get_template('program/levels.html')
    context = {'level_list': level_list,
               'program_title': program_title,
               }
    return HttpResponse(template.render(context, request))


def iterations(request, program_title, program_level):
    program_list = Program.objects.filter(name=program_title)
    level_list = ProgramLevel.objects.filter(category=program_list[0], level=program_level)
    iteration_list = Iteration.objects.filter(program=level_list[0])
    template = loader.get_template('program/iterations.html')
    context = {
        'iteration_list': iteration_list,
        'program_level': program_level,
        'program_title': program_title
    }
    return HttpResponse(template.render(context, request))


def regions(request, region):
    iteration_info_list = []
    iteration_list = Iteration.objects.filter(region=region)
    level_list = ProgramLevel.objects.all()
    program_list = Program.objects.all()
    if len(iteration_list) > 0:
        for i in iteration_list:
            i_level = level_list.get(id=i.program_id)
            i_program = program_list.get(id=i_level.category_id)
            iteration_info_list.append([i, i_level.level, i_program.name])
    template = loader.get_template('program/regions.html')
    context = {
        'iteration_info_list': iteration_info_list,
        'region': region
    }
    return HttpResponse(template.render(context, request))



