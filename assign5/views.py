from django.shortcuts import render
from .forms import UploadFileForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os
from django.conf import settings
from django.http import HttpResponse
import string
import random
import subprocess
from .models import SubResults
from django.http import JsonResponse
from multiprocessing import Process
import time




def handle_uploaded_file(filenam):
    with open('/home/vivek/BFD1/autograder' + filenam, 'r') as f:
        return f.readlines()[0][0:10]

def transfer_to_location(file_location, new_location):
    cmd = 'mkdir ' + new_location
    cmd2 = 'cp '+ file_location + ' ' + new_location + '/'
    res = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE).stdout.read()
    res = subprocess.Popen(cmd2,shell=True,stdout=subprocess.PIPE).stdout.read()
def unzipit(filex, dest):
    if filex[-3:].lower() == 'zip':
        cmd = 'unzip ' + filex + ' -d ' + dest + '/'
    elif filex[-3:].lower() == 'tar':
        cmd = 'tar -C ' + dest + '/ -xvf ' + filex
    res = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE).stdout.read()
def pomlocation(location):
    cmd = 'find '+ location + '/ -name "pom.xml"'
    res = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE).stdout.readline()
    if res == '':
        return -1
    splt = res.split("/")
    splt[-1] = ''
    res = '/'.join(splt)
    return res 
def main_autograder(pswd):
    time.sleep(10)
    dbentry = SubResults.objects.get(password = pswd)
    dbentry.mvnstarted = True
    print 'going to save now'
    dbentry.save()

def index(request):
    return HttpResponse("Hello, world. You're at the autograder.")
def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            new_sub = form.save(commit = False)
            new_sub.assignment_num = 5
            temp_str = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
            new_sub.password = temp_str
            new_sub.save()
            file_location = '/home/vivek/BFD1/autograder/media/' + str(new_sub.document)
            file_new_location = '/home/vivek/BFD1/autograder/media/' + temp_str
            new_file = file_new_location + '/' + str(new_sub.document).split('/')[1]
            transfer_to_location(file_location,file_new_location)
            unzipit(new_file, file_new_location)
            pom_XML_location = pomlocation(file_new_location)
            resultsobj = SubResults(password = temp_str, assignment_num = 5, pomlocation = pom_XML_location, eid = new_sub.eid)
            
            if pom_XML_location == -1:
                print 'yes'
                resultsobj = SubResults(password = temp_str, assignment_num = 5, eid = new_sub.eid, completed = True, errors = "Somthing went wrong - Could not find pom.xml")
                resultsobj.save()
                return render(request, 'assign5/results.html', {
                    'inputx': 'Somthing went wrong - Could not find pom.xml',
                    'EID': new_sub.eid,
                    'random_string': temp_str,
                    'next': 'stop'
                })
            else:
                resultsobj = SubResults(password = temp_str, assignment_num = 5, pomlocation = pom_XML_location, eid = new_sub.eid)
                resultsobj.save()
                passwd = str(resultsobj.password)
                p = Process(target=main_autograder, args=(passwd,))
                p.start()
                return render(request, 'assign5/results.html', {
                    'inputx': 'Found POM.XML: Please Wait. Running mvn clean package',
                    'EID': new_sub.eid,
                    'random_string': temp_str,
                    'next': 'mvn complete'
                })
    else:
        form = UploadFileForm()
    return render(request, 'assign5/upload.html', {'form':form})    


def results(request):
    passwordx = request.GET.get('password',None)
    d = SubResults.objects.get(password=passwordx)
    data = {'output': d.convert_to_string()}
    return JsonResponse(data)


# Create your views here.
