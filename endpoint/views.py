from django.shortcuts import render
from .models import EndPoints
# Create your views here.


def endPointsPBS(request):
    endpoints = EndPoints.objects.all()

    
    context = {
        "endpoints": endpoints
    }

    return render(request, "pbs.html", context)
