from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#request -> response
#request handeler
#action
#could template
def say_hello(request):
    
    return render(request,'hello.html',{'name':'Sara'})
    #return HttpResponse('Hello World')