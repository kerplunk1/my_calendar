from django.http import JsonResponse
from django.db import IntegrityError
from .models import Action

# Create your views here.
def get_actions_in_year(request, year):
    objs = Action.objects.filter(date__year=year)
    actions = {}
    for obj in objs:
        obj_date = obj.date
        date_key = f"{obj_date.year}-{obj_date.month}-{obj_date.day}"
        if date_key in actions:
            actions[date_key].append(obj.name)
        else:
            actions.update({date_key: [obj.name]}) 
    return JsonResponse(actions)


def create_new_action(request, action='SPORT'):
    try:
        row = Action(name=action.upper())
        row.save()
        if row.id:
            result = {'result': True,
                      'id': row.id,
                      'date':row.date.isoformat(),
                      'action': row.name}
            return JsonResponse(result)
    except IntegrityError as error:
        return JsonResponse({'result': False, 'error': str(error)})
    

