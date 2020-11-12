from django.shortcuts import render
from .models import toplist

# Create your views here.
def index (request):
    ur = toplist.objects.all().order_by('-id')
    return render (request,'index.html',{'ur': ur})