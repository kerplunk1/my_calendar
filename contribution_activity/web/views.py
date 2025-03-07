from django.shortcuts import render, redirect
from .calendar_package.calendar_methods import get_current_year, generate_calendar
from api.models import Action
from django.db import IntegrityError
from django.http import JsonResponse

# Create your views here.
def index(request, year=get_current_year()):
    return render(request, 'base.html', {'header': year, 'year': generate_calendar(year)})


def create_new_action(request, action='SPORT'):
    try:
        row = Action(name=action.upper())
        row.save()
        if row.id:
            return redirect('index')
    except IntegrityError as error:
        return JsonResponse({'result': False, 'error': str(error)})
    
def page_not_found(request, exception):
    return redirect('index')
