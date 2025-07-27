# from django.http import HttpResponse
from django.shortcuts import render
from .forms import BookingForm
from .models import Menu
from django.core import serializers
from .models import Booking
from datetime import datetime
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
@csrf_exempt

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')



def reservations(request):
    date = request.GET.get('date',datetime.today().date())
    bookings = Booking.objects.all()
    booking_json = serializers.serialize('json', bookings)
    return render(request, 'bookings.html',{"bookings":booking_json})


def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

# Add your code here to create new views

def bookings(request):
    if request.method == 'POST':
        # This block handles saving a new booking
        data = json.loads(request.body) # Use request.body for JSON POST data

        # Use 'data.get()' for robustness against missing keys
        first_name = data.get('first_name')
        reservation_date = data.get('reservation_date')
        reservation_slot = data.get('reservation_slot')

        # Ensure data is not None before proceeding
        if not all([first_name, reservation_date, reservation_slot]):
            return HttpResponse(json.dumps({'error': 'Missing required booking data'}), content_type='application/json')

        # Convert reservation_date string to datetime.date object for filtering
        try:
            # Assuming date format is YYYY-MM-DD from frontend
            reservation_date_obj = datetime.strptime(reservation_date, '%Y-%m-%d').date()
        except ValueError:
            return HttpResponse(json.dumps({'error': 'Invalid date format'}), content_type='application/json')


        # Check if a booking already exists for the given date and slot
        exist = Booking.objects.filter(
            reservation_date=reservation_date_obj,
            reservation_slot=reservation_slot
        ).exists()

        if not exist:
            # If no existing booking, create and save the new one
            booking = Booking(
                first_name=first_name,
                reservation_date=reservation_date_obj,
                reservation_slot=reservation_slot,
            )
            booking.save()
            return HttpResponse(json.dumps({'success': True}), content_type='application/json')
        else:
            # If booking already exists for that slot and date
            return HttpResponse(json.dumps({'error': 1}), content_type='application/json') # Use json.dumps for JSON response

    # This block handles GET requests (e.g., to fetch bookings for a specific date)
    # The pseudo-code suggests this part also returns JSON, not renders a template.
    date_str = request.GET.get('date', datetime.today().strftime('%Y-%m-%d')) # Get date string, default to today

    try:
        # Convert date string to datetime.date object for filtering
        date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        # Handle invalid date format, perhaps default to today or show an error
        date_obj = datetime.today().date() # Fallback to today's date

    bookings = Booking.objects.all().filter(reservation_date=date_obj) # Filter by the date

    booking_json = serializers.serialize('json', bookings)

    # Return serialized JSON for GET requests
    return HttpResponse(booking_json, content_type='application/json')



def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})


def display_menu_item(request, pk=None): 
    if pk: 
        menu_item = Menu.objects.get(pk=pk) 
    else: 
        menu_item = "" 
    return render(request, 'menu_item.html', {"menu_item": menu_item}) 

