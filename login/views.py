from django.shortcuts import render
from django.http import HttpResponseRedirect
from crazyforus.models import Members

def index(request):
		context = {'try_again':False}
		return render(request, 'login.html',context)

def login(request):
		if request.method == 'POST':
				member_rec = Members.objects.filter(email=request.POST['email'],password=request.POST['password'])
				if len(member_rec) == 1:
						member_id = member_rec[0].membersid
						request.session['username'] = request.POST['email']
						request.session['member_id'] = member_id
						return HttpResponseRedirect('/couples/%s/' % member_id)
				else:
						return render(request, 'login.html',{'try_again':True})
