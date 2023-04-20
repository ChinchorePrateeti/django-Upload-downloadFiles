from django.shortcuts import render, HttpResponse
from . forms import fileUploadForm
from django.contrib import messages
from .models import uploadTask

## Create your views here.

def index(request):
    if request.method == "POST":
        form = fileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['file_name']
            the_file = form.cleaned_data['the_file']
            uploadTask(file_name=name, the_file=the_file).save()

            return HttpResponse("Your File Got Uploaded Successfully....")
        else:
            return HttpResponse("error!!!")

    else:
        context = {

            'form': fileUploadForm()
        }
        return render(request, 'index.html', context)

def view_file(request):
    all_file = uploadTask.objects.all()

    return render(request, 'view.html', {'data':all_file})

