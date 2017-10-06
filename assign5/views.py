from django.shortcuts import render
from .forms import UploadFileForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os
from django.conf import settings
from django.http import HttpResponse

def handle_uploaded_file(filenam):
    with open('/home/vpradhan/dj-bdp/autograder' + filenam, 'r') as f:
        return f.readlines()[0][0:10]



def index(request):
    return HttpResponse("Hello, world. You're at the autograder.")
def upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        output = handle_uploaded_file(uploaded_file_url)
        return render(request, 'assign5/results.html', {
            'inputx': output
        })
    return render(request, 'assign5/upload.html')    


def results(request):
    context = {
        'inputx': 'nothing',
    }
    return render(request, 'assign5/results.html', context)


# Create your views here.
