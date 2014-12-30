from django.shortcuts import render
from django.http import HttpResponseRedirect
from register.forms import RegisterForm
from django.http import HttpResponse
from crazyforus.models import Members,Zipcode

def index(request):
		return render(request, 'register/index.html')

def register(request,template=None):
		#Display form for registering and show chosen template
		if request.method == 'POST':
				form = RegisterForm(request.POST)
				if form.is_valid():
						email = form.cleaned_data['email']
						bfirstname = form.cleaned_data['bfirstname']
						blastname = form.cleaned_data['blastname']
						gfirstname = form.cleaned_data['gfirstname']
						glastname = form.cleaned_data['glastname']
						websitename = form.cleaned_data['websitename']
						password = form.cleaned_data['password']
						wedding_date = form.cleaned_data['weddingdate']
						zipcode = form.cleaned_data['zipcode']
						city = form.cleaned_data['city']
						state = form.cleaned_data['state']
						active = 1 #set as active by default	
						returnnum = 0 #number of times user has logged in
						stepprocess = 0
						viewable = 1 
						saved_data = Members(bfirst_name=bfirstname,email=email,blast_name=blastname,
																		gfirst_name=gfirstname,glast_name=glastname,
																		websitename=websitename,password=password,
																		wedding_date=wedding_date,zipcode=zipcode,
																		city=city,state=state,active=active,returnnum=returnnum,
																		stepprocess=stepprocess,viewable=viewable,newsletter=0,emailnum=0,
																		emailopen=0,emailopen_date='2013-03-09')
						saved_data.save()	
						return HttpResponseRedirect('/register/')
		else:
				form = RegisterForm()
		return render(request, 'register/register.html', {'form':form})				

def websitecheck(request):
		if request.method=="GET":
				websitename = request.GET['websitename']
				cnt = Members.objects.filter(websitename=websitename).count()
				if cnt > 0: cnt = 1
				return HttpResponse(cnt, mimetype="text/plain")

def getcity(request):
		if request.method == "POST":
				if request.POST['zipcode']:
						zip = Zipcode.objects.filter(zipcode=request.POST['zipcode'])
						#return first result
						if zip:
								city = str(zip[0].city)
								state = str(zip[0].stateabbr)
								result = str(state+","+city)
						else:
								result = "none"
						return HttpResponse(result, mimetype="text/plain")
		if request.method == "GET":	
				if request.GET['zipcode']:
						zip = Zipcode.objects.filter(zipcode=request.GET['zipcode'])
						#return first result
						if zip:
								city = str(zip[0].city)
								state = str(zip[0].stateabbr)
								result = str(state+","+city)
						else:
								result = "none"
						return HttpResponse(result, mimetype="text/plain")

