from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from store.models.product import Product
from store.models.customer import Customer
from django.http import HttpResponse 
from django.views import View

class Login(View):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")
        customer = Customer.get_customer_by_email(email)

        error_message = None
        
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session["customer"] = customer.id
                return redirect("homepage")
            else:
                error_message = "Email or Password invalid !!"
        else:
            error_message = "Email or Password invalid !!"
        
        return render(request, "login.html", {"error" : error_message})

def logout(request):
    request.session.clear()
    return redirect("homepage")