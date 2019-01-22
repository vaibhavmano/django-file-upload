from django.http import HttpResponse
from django.shortcuts import render
from .models import Name ,File
from .forms import NameForm 
# Create your views here.
# def index(request):
#     return HttpResponse("Hello World!")
def greet(request):
    total_name = Name.objects.all().get(id=1)
    # last_name = Name.objects.all().get(id=1)
    # context = {
    #     'first_name': first_name,
    #     'last_name': last_name,
    #     }
    return render(request, 'index.html', {'name': total_name})

def add_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Name added')
    else:
        form = NameForm()
    return render(request,'index.html', {'name_form': form})