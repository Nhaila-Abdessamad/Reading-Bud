from django.shortcuts import render


rooms = [
    {'id':1, 'name': 'Elon Musk'},
    {'id':2, 'name': 'Nick Bostrom'},
    {'id':3, 'name': 'Ray Kurzwell'},
]

def home(request):
    context = {'rooms':rooms}
    return render(request, 'base/home.html', context )


def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room':room}
    return render(request, 'base/room.html', context)
# Create your views here.
# this is where we render what the user clicks on.
