from django.shortcuts import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the program index.")


def details(request, program_title):
    return HttpResponse("This is a list of levels offered for %s." % program_title)


def iterations(request, program_title, level_id):
    return HttpResponse("This is a list of upcoming sessions for level "
                        + level_id+" of "+program_title+".")




