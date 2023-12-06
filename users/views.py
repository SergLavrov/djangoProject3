from django.http import HttpResponse, HttpRequest
from django.template import loader
from .models import User

# Create your views here.

def register(request: HttpRequest) -> HttpResponse:
    try:
        user = User(first_name='Alex', last_name='Alinov', age=20, phone='417-25-89', address='Moscow')
        user1 = User(first_name='Fill', last_name='Filatov', age=25, phone='917-25-99', address='Brest')
        user2 = User(first_name='Vlad', last_name='Vladov', age=21, phone='715-55-10', address='Vitebsk')
        user3 = User(first_name='Ivan', last_name='Ivanov', age=30, phone='546-05-00', address='Piter')
        user4 = User(first_name='Nazar', last_name='Nazimov', age=27, phone='917-66-87', address='Moscow')
        list_users = [user, user1, user2, user3, user4]
        for user in list_users:
            user.save()
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse({"error_message": f"Error: {e}"})



def list_users(request: HttpRequest) -> HttpResponse:
    users = User.objects.all().values()
    template = loader.get_template('users/list.html')
    data = {
        'header': 'Список пользователей',
        'users': users,
    }
    return HttpResponse(template.render(data))


def get_user_profile(request: HttpRequest, id: int) -> HttpResponse:
    try:
        user = User.objects.get(id=id)
        template = loader.get_template('users/user_profile.html')
        data = {
            'header': 'Профиль пользователя',
            'user': user,
        }
        return HttpResponse(template.render(data, request))
    except:
        return HttpResponse("Error")
