from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from store.models.product import Product
from store.models.customer import Customer
from django.http import HttpResponse 
from django.views import View


class Signup(View):

    def get(self, request):
        return render(request, "signup.html")

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        email = postData.get('email')
        phone = postData.get('phone')
        password = postData.get('password')

        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email,
        }

        customer = Customer(first_name = first_name, last_name = last_name, email = email, phone = phone, password = password)

        error_message = self.validateCustomer(customer)

        if not error_message:  
            customer.password = make_password(customer.password)
            customer.register()  
            return redirect("homepage")      

        else:

            data = {
                'error': error_message,
                'values': value,
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self, customer):

        error_message = None

        if (not customer.first_name):
            error_message = "first name required !!"
        elif len(customer.first_name) < 4:
            error_message = "first name must be 4 character long !!"
        elif (not customer.last_name):
            error_message = "last name required !!"
        elif len(customer.last_name) < 4:
            error_message = "last name must be 4 character long !!"
        elif (not customer.phone):
            error_message = "phone number required !!"
        elif len(customer.phone) < 10:
            error_message = "phone number must be of 10 digits !!"
        elif len(customer.password) < 5:
            error_message = "password must be 5 characters long !!"
        elif len(customer.email) < 5:
            error_message = "email must be 5 characters long !!"
        elif customer.isExists():
            error_message = "email already registered !!"

        return error_message