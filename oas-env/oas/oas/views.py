from django.shortcuts import render



def home(request):
    data = {
        "id": "1",
 }
    return render(request,'index.html',data)