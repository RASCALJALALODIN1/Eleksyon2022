from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls.conf import re_path

from Dzellalsys.forms import voteform
from .models import *

def Mainpage(request):
	if request.method == 'POST':
		fname= request.POST['fname']
		mname = request.POST['mname']
		sname = request.POST['sname']
		age = request.POST['age']
		rvote = request.POST['rvote']
		region = request.POST['region']
		pnum = request.POST['pnum']
		pres = request.POST['pres']
		vpres = request.POST['vpres']
		political_party = request.POST['political_party']
		a = votes.objects.filter(region= 'Cavite').count()
		b = votes.objects.filter(region= 'Batangas').count()
		c = votes.objects.filter(region= 'laguna').count()
		d = votes.objects.filter(region= 'Rizal').count()
		e = votes.objects.filter(region= 'Quezon Province').count()
		numvotes.objects.create(cavite = a, batangas = b, laguna=c, rizal=d, qprov=e)
		print(a,b,c,d, e)
		votes.objects.create(fname = fname, mname = mname, sname=sname, age=age,
		rvote=rvote, region=region, pnum=pnum, pres=pres, 
		vpres=vpres, political_party = political_party)
	return render(request,'mainpage.html')
def Votesperregion(request):

	anumvotes = numvotes.objects.all()
	return render(request,'VotesPerRegion.html',{'numvotes':anumvotes})
def Responses(request):
	avotes = votes.objects.all()
	return render(request,'Responses.html',{'votes':avotes})
def Index(request):
	return render(request,'1st page.html')

def edit(request, id):
	vote = votes.objects.get(id=id)
	form = voteform(instance=vote)
	if request.method == 'POST':
		form = voteform(request.POST, instance = vote)
		if form.is_valid():
			form.save()
			return redirect('/Responses')

	return render(request, 'edit.html', {'form':form})
		
def delete(request, id):
    v = votes.objects.get(id=id)
    for x in votes.objects.only('id'):

        print(x)
        if v == x:
            x = votes.objects.get(id=id).delete()
            break
    return redirect('/Responses')

# def MainPage(request):

# 	if request.method == "POST":
# 		Registration.objects.create(NewFirstName = request.POST['FirstName'],
# 			NewMiddleName= request.POST['Middlename'],
# 			NewSurname= request.POST['Surname'],
# 			NewAge= request.POST['Age'],
# 			Rdbtn=request.POST['RegVote'],
# 			NewQstn1 =request.POST['What'],
# 			DrpbxBasis=request.POST['basis'],
# 			DrpbxElection=request.POST['Pres'],
# 			DrpboxVC=request.POST['VPres'],)

# 		return redirect('/')
# 	reglist = Registration.objects.all()
# 	return render(request, 'mainpage.html',{'registered_Eleksyon' :reglist})




