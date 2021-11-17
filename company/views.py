from django import forms
from django.db import models
from django.shortcuts import render
from django.http import HttpResponse
from company.models import cars,emp,project
from django.shortcuts import redirect
from  .forma import forminsert,form_update

from django.views.generic import ListView 
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    # car1=cars.objects.create(car_number=1)
    # car2=cars.objects.create(car_number=2)
    # car3=cars.objects.create(car_number=3)

    # emp1=emp.objects.create(emp_name="fathi",emp_number=100,car_id=car1)
    # emp2=emp.objects.create(emp_name="ahmed",emp_number=200,car_id=car2)
    # emp3=emp.objects.create(emp_name="ali", emp_number=300,car_id=car3)

    # project.objects.create(p_number=10, title="first",emp_id=emp1)
    # project.objects.create(p_number=20, title="sec",emp_id=emp2)
    # project.objects.create(p_number=30, title="third",emp_id=emp3)
    
    
    # a=project.objects.all()
    # print(a)
    # project.objects.filter(p_number=1).delete()
    # emp.objects.filter(emp_name='fathi').update(emp_name='yehya')
    
    #     print(x.emp_id.emp_name)
    # print(Array[0][2].emp_name)
    if ('user' in request.session):
        return render(request,'company/all.html',{'data':project.objects.all()})
    else:
        return redirect('/')

def insert(request,):
    if ('user' in request.session):
        forma=forminsert(request.POST)
        if forma.is_valid():
            project.objects.create(p_number=request.POST['project_number'], title=request.POST['title'],)   
            print(request.POST['project_number'])
        # car1=cars.objects.create(car_number=5000000)
        # emp1=emp.objects.create(emp_name="fathi",emp_number=10000000,car_id=car1)
        # project.objects.create(p_number=p_number, title=title,emp_id=emp1)
        return render(request,'company/insert.html',{'forma':forma})
    else:
        return redirect('/')


def delete(request,id):
    if ('user' in request.session):
        project.objects.filter(id=id).delete()
        return redirect('/company/')
    else:
        return redirect('/')
def update(request):
    if ('user' in request.session):
        print(request.POST)
        form_up=form_update(request.POST)
        if form_up.is_valid():  
            project.objects.filter(p_number= request.POST["project_number"]).update(title=request.POST["title"])
            return redirect('/company/',request)
        return render(request,'company/update.html',{'form_up':form_up})
    else:
        return redirect('/')
    

class listall(ListView):
    model=project
