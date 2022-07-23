# from multiprocessing import context
# from django.shortcuts import render, HttpResponse
from multiprocessing import context
from django.template import RequestContext
# from setuptools import required
from django.http import HttpResponse
from django.shortcuts import render,redirect
# from.forms import usersForm
from datetime import datetime
from home.models import Contact
# from home.forms import Register
from django.contrib import messages

# Create your views here.
def index(request):
    # context = {
    #     "variable1":"Subhasis sahoo",
    #     "variable2":"Chandan sahoo"
    # }
    messages.success(request,"This is the text message")
    
    # return HttpResponse("This is HomePage"),
    return render(request,'home.html')
def about(request):
    # return HttpResponse("This is AboutPage")
    return render(request,'about.html')

def services(request):
    # return HttpResponse("This is ServicesPage")
    return render(request,'services.html')
def faq(request):
    # return HttpResponse("This is ServicesPage")
    return render(request,'FAQ.html')
def register(request):
    # return HttpResponse("This is ServicesPage")
    return render(request,'register.html')
# def login(request):    
#     return render(request,'login.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        text = request.POST.get('text')
        contact = Contact(name=name, email=email, phone=phone, text=text, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message sucessfully sent.')
    return render(request,'contact.html')
    # return HttpResponse("This is ContactPage")
    
# def register(request):    
#     if request.method == 'POST':
        
#             fname = form.cleaned_data.get('username')
#             fname = request.POST.get('fname')
#             lname = request.POST.get('lname')
#             email = request.POST.get('email')
#             number = request.POST.get('number')
#             address = request.POST.get('address')
#         # password = request.POST.get('password')
#         register = Register(fname=fname,lname=lname, email=email, number=number, address=address, date=datetime.today())
#         register.save()
#         messages.success(request, 'Your Request was sucessfully sent.')
       
#         return render(request,'register.html',{'form':form})
    

# def blog(request):
    # context = {
    #     "variable1":"Subhasis sahoo",
    #     "variable2":"Chandan sahoo"
    # }
    


# messages.debug(request, '%s SQL statements were executed.' % count)
# messages.info(request,'Three credits remain in your account.')
# messages.success(request, 'profile details updated.')
# messages.waring(request, 'your account expires in three days.')
# messages.error(request,'document deleted.')


# def register(request):    
#     if request.method == 'POST':           
#         fname = request.POST.get('fname')
#         lname = request.POST.get('lname')
#         email = request.POST.get('email')
#         number = request.POST.get('number')
#         password = request.POST.get('password')
#         rpassword = request.POST.get('rpassword')
#         register = Register(fname=fname,lname=lname, email=email, number=number, password=password,rpassword=rpassword, date=datetime.today())
#         register.save()
#         messages.success(request, 'Your Request was sucessfully sent.')
#     return render(request,'register.html')

# def register(request):    
#     if request.method == 'POST': 
#         fm = Register(request.POST)
#         if fm.is_valid():
#             print('Form Validated')
#             print('fname',fm.clear_data['fname'])
#             print('lname',fm.clear_data['lname'])
#             print('email',fm.clear_data['email'])
#             print('number',fm.clear_data['number'])
#             print('password',fm.clear_data['password'])
#             print('rpassword',fm.clear_data['rpassword'])

# def register(request):
#     if request.method =='POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request,f'Congratulations ! Account has been created and you can login {username}!')
#             return redirect('login')
#     else:
#         form = UserRegisterForm()
#     return render(request,'users/register.html',{'form':form})