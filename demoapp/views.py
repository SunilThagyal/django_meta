from django.shortcuts import render
from django.http import HttpResponse  # Correct import
from demoapp.models import Users
def index(request):
    # return HttpResponse('hello')
    # sys.exit()
    return render(request, "dashboard/index.html")  # Updated line

def mainMainagerList(request):
    users = Users.objects.all()
    print('HELLO')
    return render(request, "admin/main-managers/list.html",{'users':users})