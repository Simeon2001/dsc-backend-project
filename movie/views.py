from django.shortcuts import render
from .models import toplist
from .forms import moviecreate
# Create your views here.
def index (request):
    ur = toplist.objects.all().order_by('-id')
    comm = None
    if  request.POST == 'POST':
        form = moviecreate(request.POST)
        if form.is_valid():
            comm =form.save(commit=False)
            comm.save()
    else:
        form = moviecreate()
    return render (request,'index.html',{'ur': ur,'form':form})
    
def home (request):
    comm = None
    if request.method == 'POST':
        form = moviecreate(request.POST)
        if form.is_valid():
            comm = form.save(commit=False)
            comm.save()
    
    else:
	    form = moviecreate()
        
    return render(request, 'contact.html', {'form': form})    

            