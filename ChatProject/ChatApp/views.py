from django.shortcuts import render,redirect
from .models import Room,Message

# Create your views here.
def HomePage(request):
    if request.method == 'POST':
        username = request.POST['username']
        room = request.POST['room']
        try:
            get_room = Room.objects.get(room_name=room)
            return redirect('room', room_name=room,username=username)
        except Room.DoesNotExist:
            new_room = Room(room_name = room)
            new_room.save()
            return redirect('room', room_name=room,username=username)

    return render (request,'index.html')

def MessageView(requset,room_name,username):

    get_room = Room.objects.get(room_name=room_name)

    if requset.method == "POST":
        message = requset.POST['message']
        print(message)
        
        new_message = Message(room=get_room,sender=username,message=message)
        new_message.save()

    get_room = Room.objects.get(room_name=room_name)
    get_messages=Message.objects.filter(room=get_room)

    context = {
        "messages": get_messages,
        "user": username,
    }

    return render(requset,'message.html',context)