from django.shortcuts import render
def home(request):
    return render(request, 'index.html')
def store(request):
    return render(request, 'store list.html')
