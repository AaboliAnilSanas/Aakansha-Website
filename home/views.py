from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User


def index(request):
    return render(request, 'index.html')


def login_request(request):
    if request.method == 'POST' and 'form1' in request.POST:    
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['mobile_no']
        password = request.POST['password']
        user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email, username=username, password=password)
        user.save()
        return redirect('/login/')

    if request.method == 'POST' and 'form2' in request.POST:
        username = request.POST['mobile_no1']
        password1 = request.POST['password1']
        user = authenticate(username=username, password=password1)
        if user is not None:
            login(request, user)
            return redirect('index')
    return render(request, 'login.html')

def logout_request(request):
    logout(request)
    return redirect("index")
def index(request):
    return render(request,'index.html')
def booked(request):
    return render(request,'booked.html')
def cart(request):
    return render(request,'cart.html')
def contactus(request):
    return render(request,'contactus.html')
def filter(request):
    return render(request,'filter.html')
def LocalStore(request):
    return render(request,'LocalStore.html')
def product(request):
    return render(request,'product.html')
def productssfe(request):
    return render(request,'productssfe.html')
def sports_acces(request):
    return render(request,'sports_acces.html')
def sports_store(request):
    return render(request,'sports_store.html')
def sports_events(request):
    return render(request,'sports_events.html')
def TicketBooking(request):
    return render(request,'Ticket Booking.html')


    
    
   
