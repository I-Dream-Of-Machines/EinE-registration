from django.shortcuts import HttpResponse
from django.template import loader
from .models import Program
from .models import Iteration

# Create your views here.


def index(request):
    program_list = Program.objects.all()
    template = loader.get_template('program/index.html')
    context = {'program_list': program_list,
               }
    return HttpResponse(template.render(context, request))


def details(request, program_title):
    return HttpResponse("This is a list of levels offered for %s." % program_title)


def iterations(request, program_title, level_id):
    return HttpResponse("This is a list of upcoming sessions for level "
                        + level_id+" of "+program_title+".")




