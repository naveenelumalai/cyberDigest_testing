from django.shortcuts import render
from django.http import HttpResponse
from second_app.models import CyberStories
# Create your views here.

def index(request):
    return render(request,'index.html')

def digest(request):
    return render(request, 'digest.xml')

def dict(request):
    people = {'a': {'name': 'John', 'age': '27', 'sex': 'Male'},
          'b': {'name': 'Marie', 'age': '22', 'sex': 'Female'}}
    return render(request, 'dict.html', context=people['a'])

def cyberdigest(request):
    cyber_digest_list = CyberStories.objects.order_by('Title')
    cyber_dict = {'access_records':cyber_digest_list}
    return render(request,'cyberdigest.html',context=cyber_dict)

def testingtemplate(request):
    cyber_digest_list = CyberStories.objects.order_by('-Published')
    cyber_dict = {'access_records':cyber_digest_list}
    return render(request,'testingtemplate.html',context=cyber_dict)

def fromscratch(request):
    cyber_digest_list = CyberStories.objects.order_by('-Published')
    cyber_dict = {'access_records':cyber_digest_list}
    return render(request,'fromscratch.html',context=cyber_dict)
