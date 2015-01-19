# -*- coding:utf8 -*-

# Create your views here.
from django.http import HttpResponse,Http404
from django.template import Template,Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
import datetime

from django.db.models import *
from moonbuck.mis.models import *

def homepage(request):
    return render_to_response('index.html',locals())

def crmHome(request):
    return render_to_response('CRM首页.html',locals())

def crmSearch(request):
    return render_to_response('CRM检索页面.html',locals())

def crmSearchResult(request):
    if request.method == 'GET':
        query = request.GET
        pass
    elif request.method =='POST':
        query = request.POST
        pass
    else:
        return render_to_response('CRM查询结果.html',locals())

def prmHome(request):
    return render_to_response('PRM首页.html',locals())

def crm_adduser(request):
    errors=[]
    if request.method == 'POST':
        if not errors:
            userno=request.GET['userno']
            username=request.GET['username']
            email=request.GET['email']
            mob_num=request.GET['mob_num']
            birthyear=request.GET['birthyear']
            birthmonth=request.GET['birthmonth']
            birthday=request.GET['birthday']
            address=request.GET['address']
            cryear=request.GET['cryear']
            crmonth=request.GET['crmonth']
            crday=request.GET['crday']

            temp=customer(cuId=userno,cuName=username,cuEmail=email,cuPhone=mob_num,cuCreate=crday)
            temp.save()

            return HttpResponseRedirect('/crm/')
    
    return render_to_response('add_customer.html',locals())


def crm_user_search(request):
    return render_to_response('CRM检索页面.html',locals())

def crm_user_searchresult(request):
    if request.method == 'GET':
        if 'participant1' & 'textcontent1' in request.GET:
            participant1=request.GET['participant1']
            textcontent1=request.GET['textcontent1']
            if participant1 == 2:
                record=mis.objects.filter(cuName=textcontent1)
            return render_to_response('CRM查询结果.html',locals())
        else:
            return render_to_response('CRM检索页面.html',locals())
