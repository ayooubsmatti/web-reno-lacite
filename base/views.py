from django.shortcuts import render
from .forms import DemendeUnAppelForm

from base.models import Service

# Create your views here.
def home(request):
    services = Service.objects.all()
    form = DemendeUnAppelForm
    if request.method == 'POST':
        form = DemendeUnAppelForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'services':services,'form':form}
    return render(request, 'base/home.html',context)


def service(request,pk):
    services = Service.objects.all()
    service = Service.objects.get(id=pk)
    context = {'services':services ,
                'service' : service}
    return render(request, 'base/service.html',context)

def about(request):
    services = Service.objects.all()
    context = {'services':services ,
                'service' : service}
    return render(request,'base/about.html',context )

def contact(request):
    services = Service.objects.all()
    context = {'services':services ,
                'service' : service}
    return render(request,'base/contact.html',context )


