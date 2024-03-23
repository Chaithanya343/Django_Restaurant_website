from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
# from .forms import ReservationForm
def homepage(request):
    return render(request,"index.html")
def aboutus(request):
    return render(request,"aboutus.html")
def menu(request):
    return render(request,"menu.html")

def eventbooking(request):
    return render(request,"eventbooking.html")
def location(request):
    return render(request,"location.html")

def reservation(request):
    # form = ReservationForm()
    # data = {"form": form}
    return render(request,"reservation.html")


def is_valid_input(user_input):
    # Check if the input contains only alphabetic characters, spaces, and dots
    return all(char.isalpha() or char.isspace() or char == '.' for char in user_input)

def resop(request):
    data={}
    try:
        if request.method=="POST":
            n=request.POST.get('name')
            try:
                # Check if the input is valid
                if is_valid_input(n):
                    n1 = request.POST.get('name')
                    n2 = int(request.POST.get('name'))
                    # total=n2+3
                    data = {
                        'name': n,
                        'phone': n1,
                        'output': n2,
                    }
                else:
                    raise ValueError(
                        "Invalid input. Please enter valid name")

            except ValueError as ve:
                return render(request, 'reservation.html', {'error_message': str(ve)})

    except:
        pass
    return render(request,"reservation_op.html",data)