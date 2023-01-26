from django.shortcuts import render
from app.models import *
# Create your views here.
from django.http import HttpResponse


def insert_topic(request):
    tn=input('Enter topic_name : ')
    T=Topic.objects.get_or_create(topic_name=tn)[0]
    T.save()

    return HttpResponse('Topic added successful')

def insert_webpage(requst):
    tn=input('Enter topic_name : ')
    name=input('enter name : ')
    url=input('enter url : ')
    T=Topic.objects.get_or_create(topic_name=tn)[0]
    T.save()
    W=Webpage.objects.get_or_create(topic_name=T,name=name,url=url)[0]
    W.save()

    return HttpResponse('Webpage inserted successfully')


def insert_accessrecords(request):
    tn=input('Enter topic : ')
    name=input('Enter name : ')
    url=input('Enter url : ')
    date=input('enter date : ')
    T=Topic.objects.get_or_create(topic_name=tn)[0]
    T.save()
    W=Webpage.objects.get_or_create(topic_name=T,name=name,url=url)[0]
    W.save()
    A=AccessRecords.objects.get_or_create(name=W,date=date)[0]
    A.save()


    return HttpResponse('AccessRecord added successfully')