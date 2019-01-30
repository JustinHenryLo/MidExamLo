from django.shortcuts import render,redirect
from .models import Candidate,Position,Vote
from .forms import CandidateModelForm,PositionModelForm
from datetime import datetime 
# Create your views here.
def index(request):
    context = {} #params
    candidates = Candidate.objects.all()
    context['candidates']=candidates
    return render(request,"index.html",context)

def create(request):
    context={}
    if(request.method == 'POST'):
        form = CandidateModelForm(request.POST)
        if(form.is_valid()):
            form.save()#this fucking returns the object it saves !!!!!!!!!!
            return redirect('votes:index')
        else:
            context['candidate_form']=form
            return render(request,'candidate_create.html',context)
    else:
        form = CandidateModelForm()
        context['candidate_form']=form
        return render(request,'candidate_create.html',context)

def create_position(request):
    context={}
    if(request.method == 'POST'):
        form = PositionModelForm(request.POST)
        if(form.is_valid()):
            form.save()#this fucking returns the object it saves !!!!!!!!!!
            return redirect('votes:index')
        else:
            context['position_form']=form
            return render(request,'position_create.html',context)
    else:
        form = PositionModelForm()
        context['position_form']=form
        return render(request,'position_create.html',context)

def detail(request, c_id):
    context={}
    c = Candidate.objects.get(id=c_id)
    votes_total = Vote.objects.filter(candidate = c).count
    context['candidate'] = c
    context["votes_total"] = votes_total
    return render(request,"detail.html",context)

def update(request, c_id):
    context ={}
    context["id"]=c_id
    c = Candidate.objects.get(id=c_id)
    if(request.method == 'POST'):
        form = CandidateModelForm(request.POST, instance=c)
        if form.is_valid():  #data val
            form.save()
            return redirect('votes:detail',c_id)
        else:
            context['candidate_form']=form
            return render(request,'update.html',context)
    else:
        context['candidate_form'] =CandidateModelForm(instance=c)
        return render(request,"update.html",context)

def vote(request, c_id):
    context ={}
    c = Candidate.objects.get(id = c_id)
    Vote(candidate = c, vote_datetime= datetime.now()).save()
    return redirect('votes:detail',c_id)
    