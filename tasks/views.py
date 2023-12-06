from django.http import HttpResponse, HttpRequest
from django.template import loader
from .models import Tasks

# Create your views here.

def register(request: HttpRequest) -> HttpResponse:
    try:
        task1 = Tasks(task_name='Task1', number='One', execute_time='10')
        task2 = Tasks(task_name='Task2', number='Two', execute_time='11')
        task3 = Tasks(task_name='Task3', number='Three', execute_time='5')
        task4 = Tasks(task_name='Task4', number='Four', execute_time='7')
        task5 = Tasks(task_name='Task5', number='Five', execute_time='3')
        list_tasks = [task1, task2, task3, task4, task5]
        for task in list_tasks:
            task.save()
        return HttpResponse("OK")
    except:
        return HttpResponse("Error")


def list_tasks(request: HttpRequest) -> HttpResponse:
    tasks = Tasks.objects.all().values()
    template = loader.get_template('tasks/list.html')
    data = {
        'header': 'Список задач',
        'tasks': tasks,
    }
    return HttpResponse(template.render(data))



def get_task_profile(request: HttpRequest, id: int) -> HttpResponse:
    try:
        task = Tasks.objects.get(id=id)
        template = loader.get_template('tasks/task_profile.html')
        data = {
            'header': 'Information about task',
            'task': task,
        }
        return HttpResponse(template.render(data, request))
    except:
        return HttpResponse("Error")