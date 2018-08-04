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


def iterations(request, program_title, level):
    program_list = Program.objects.filter(name=program_title)
    level_list = ProgramLevel.objects.filter(category=program_list[0], level=level)
    iteration_list = Iteration.objects.filter(level)
    return HttpResponse("This is a list of upcoming sessions for level "
                        + level_id+" of "+program_title+".")




