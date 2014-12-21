from django.shortcuts import render
from django.http import HttpResponseRedirect
from couples.forms import UploadMainPic
from crazyforus.models import Members
from crazyforus.models import Welcome, Ourstories
import datetime

def index(request, members_id=None):
		#this renders the main admin page
		if 'member_id' in request.session:
				members_id = request.session['member_id']
		if not members_id:
				return HttpResponseRedirect('/login/')
		form = UploadMainPic()
		hero_thumb = get_hero_thumb(members_id)
		context = {'form':form, 'members_id':members_id, 'hero_image':hero_thumb, 'username': request.session['username']}
		return render(request,'index.html',context)

def get_hero_thumb(members_id):
		member = Members.objects.get(pk=members_id)
		hero_image = member.hero_image
		return hero_image		

def welcome(request):
		welcome = Welcome.objects.get(membersid=request.session['members_id'])				
		context = {'title': welcome.title}
		return render(request, 'welcome.html', context)

def our_stories(request):
		stories = Ourstories.objects.filter(members=request.session['member_id'])
		male_story = female_story = ""
		for story in stories:
				if store.sex == 'male':
						male_story = store.body
				else:
						female_story = store.body
		context = {'female_story': female_story, 'male_story': male_story}
		return render(request, 'our_stories.html', context)

def update_stories(request):
		member_id = int(request.session['member_id'])
		context = ''
		if request.method == 'POST' and member_id:
				member_key = Members.objects.get(pk=member_id)
				male_story = request.POST['story_1'] #Request Variables are sent with different names, because this could be coming from two men...or two women.
				female_story = request.POST['story_2']
				rec_male, created_m  = Ourstories.objects.get_or_create(members=member_key, sex='male', 
																								defaults={'date': datetime.datetime.now(), 'body': male_story, 'active': 1})
				rec_female, created_f = Ourstories.objects.get_or_create(members=member_key, sex='female', 
																								defaults={'date': datetime.datetime.now(), 'body': female_story, 'active': 1})
				if not created_m:
						rec_male.body = male_story
						rec_male.save()
				if not created_f:
						rec_female.body = female_story
						rec_female.save()
				context = {'female_story': female_story, 'male_story': male_story} 
		else:
				return HttpResponseRedirect('/login.html')
		return render(request, 'our_stories.html', context)

def upload_main_pic(request, members_id=None):
		if request.method == 'POST':
				form = UploadMainPic(request.POST, request.FILES)
				status = "Post Received"
				if form.is_valid():
						status = "Form Is Valid"
						member = Members.objects.get(pk=members_id)
						member.hero_image = request.FILES['hero_image']
						member.save()
						hero_thumb = get_hero_thumb(members_id)
				else:
						status = "Post Recd, Form not valid"
		else:
				status = "Request Not Sent"
				form = UploadPic()

		context = {'form':form, 'members_id': members_id, 'hero_image': hero_thumb}
		return render(request, 'index.html', context)
