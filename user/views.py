from django.shortcuts import redirect, render
from .forms import Loginform
from  .models import  Myuser
# Create your views here.
def login(request):
    context={}
    form=Loginform()
    if(request.method=='GET'):
        context['form']=form
        return render(request,'user/login.html',context)
    else:
        try:
            myuser= Myuser.objects.get(Password=request.POST['Password'],Username=request.POST['Username'])
            request.session['user']=myuser.id
            context['user']=myuser
            print(myuser)
            return redirect('/company/',context)
        except:
            context['msg']='user pass or name invalid'
        return render( 'user/login.html', context)
def logout(request):
    #clear session
    request.session.clear()
    #redirect to login page
    context={}
    context['form']=Loginform()
    # return render(request,'user/login.html',context)
    return redirect('/')