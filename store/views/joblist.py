from django.shortcuts import render, redirect
from store.models.joblist import Joblist

from store.models.skillcat import Skillcat
from store.models.ecat import Ecat
from store.models.lcat import Lcat
from store.models.icat import Icat
from store.models.scat import Scat

from django.views import View

class Jb(View):

    def post(self, request):
        joblist = request.POST.get('joblist')
        cart = request.session.get('cart')

        if cart:
            cart[joblist] = 1    
        else:
            cart = {}
            cart[joblist] = 1
        request.session['cart'] = cart
        print(request.session['cart'])
        return redirect("joblist")

    def get(self, request):      
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
                
        joblists = None

        skillcats = Skillcat.get_all_skillcats()
        skillcatID = request.GET.get('skillcat')

        ecats = Ecat.get_all_ecats()
        ecatID = request.GET.get('ecat')

        lcats = Lcat.get_all_lcats()
        lcatID = request.GET.get('lcat')

        icats = Icat.get_all_icats()
        icatID = request.GET.get('icat')

        scats = Scat.get_all_scats()
        scatID = request.GET.get('scat')

        if skillcatID:
            joblists = Joblist.get_all_joblists_by_skillcatid(skillcatID)
        elif ecatID:
            joblists = Joblist.get_all_joblists_by_ecatid(ecatID)
        elif lcatID:
            joblists = Joblist.get_all_joblists_by_lcatid(lcatID)
        elif icatID:
            joblists = Joblist.get_all_joblists_by_icatid(icatID)
        elif scatID:
            joblists = Joblist.get_all_joblists_by_scatid(scatID)
        else:   
            joblists = Joblist.get_all_joblists()   

        data = {}
        data['joblists'] = joblists    
        data['skillcats'] = skillcats
        data['lcats'] = lcats
        data['icats'] = icats
        data['scats'] = scats

        return render(request, 'joblist.html', data)