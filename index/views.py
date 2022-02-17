from django.shortcuts import render
from django.utils import timezone

def index(request):
    now = timezone.now()
    print(type(now.year.__str__()))
    return render(request, 'index.html')
