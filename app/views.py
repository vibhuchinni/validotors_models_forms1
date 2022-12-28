from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
# Create your views here.
def insert_topic(request):
    form=TopicForm()
    d={'form':form}
    if request.method=='POST':
        fd=TopicForm(request.POST)
        if fd.is_valid():
            fd.save()
            return HttpResponse('insert_topic is done')
    return render(request,'insert_topic.html',d)


