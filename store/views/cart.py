from django.views import View
from django.shortcuts import render, redirect
from store.models.joblist import Joblist

class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        joblists = Joblist.get_joblists_by_id(ids)

        return render(request, "cart.html", {'joblists' : joblists})