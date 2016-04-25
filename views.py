from django.shortcuts import render
from .models import Signin,Login


def index(request):
	return render(request,'index.html')

def form(request):
	return render(request,'form.html')

def form1(request):
	if request.POST:
		uname = request.GET.get('uname')
        mnumber= request.GET.get('mnumber')
        mailid= request.GET.get('mailid')
        address= request.GET.get('address')
        password= request.GET.get('password')
        cofirmpassword= request.GET.get('cofirmpassword')
        q=Signin(uname=uname,mnumber=mnumber,mailid=mailid,address=address,password=password,cofirmpassword=cofirmpassword)
        q.save()
        return render(request,'loginform.html')

		
		
		
		













