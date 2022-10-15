from django.shortcuts import render
from django.http import HttpResponse
from Registration_1.models import Course, Batch, Student
# Create your views here.
def index(Request):
    return HttpResponse("<h1>Welcome to Prime Intuit Registration page</h1>")
def Home(request):
    #return HttpResponse("<h1> Welcome to prime Intuit Home page</h1>")
    batch_list=Batch.objects.order_by('batch_ID')
    #batch_list = Batch.objects.raw('select * from Registration_1 Batch where start_date')
    data_dict={'access_record':batch_list,'Insert_ME':"I am a text from Registration_1/Views.py"}

#    my_dict={'Insert_ME':"I am a text from Registration_1/Views.py now from sub templates"}
    return render(request,'Restration/index.html',context=data_dict)