from django.shortcuts import render
def home(request):
    return render(request, 'index.html')
def buisnes(request):
    return render(request, 'buisneses.html')
def icon(request):
    return render(request, 'icons.html')