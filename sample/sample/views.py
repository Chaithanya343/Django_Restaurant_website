from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ReservationForm
from home.models import home
from aboutus.models import Caboutus
import re

def homepage(request):
    home_data = home.objects.all().order_by("para_num")
    data={"home_data":home_data}
    # for i in home_data:
    #     print(i.home_desc)
    return render(request,"index.html",data)
def aboutus(request):
    aboutus_data=Caboutus.objects.all() [:5]
    data={"aboutus_data":aboutus_data}
    return render(request,"aboutus.html",data)
def menu(request):
    return render(request,"menu.html")

def eventbooking(request):
    return render(request,"eventbooking.html")
def location(request):
    return render(request,"location.html")

def reservation(request):
    # fn = ReservationForm()
    # data = {"form": fn}
    return render(request,"reservation.html")


def is_valid_input(user_input):
    # Check if the input contains only alphabetic characters, spaces, and dots
    return bool(re.match(r'^[A-Za-z\s]+$', user_input))


from django.shortcuts import render, redirect


def resop(request):
    if request.method == "POST":
        name = request.POST.get('name')
        try:
            # Validate the input name
            if not is_valid_input(name):
                raise ValueError("Invalid input. Please enter a valid NAME without numbers or special characters.")

            phone = str(request.POST.get('countryCode')) + str(request.POST.get('phone'))
            people = int(request.POST.get('people'))

            # If everything is valid, proceed to render the output
            data = {
                'name': name,
                'phone': phone,
                'output': f"Booking confirmed for {people} people under the name {name}.",
            }
            return render(request, "reservation_op.html", data)

        except ValueError as ve:
            # Redirect back to the /reservation/ page with an error message
            return redirect('/reservation/?error_message=' + str(ve))

    # If not a POST request, render the reservation form
    return render(request, "reservation.html")
