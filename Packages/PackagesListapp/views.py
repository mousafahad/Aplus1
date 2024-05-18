
from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from .forms import UserRegistrationForm
from django.shortcuts import render, redirect
from .models import CarWashService
from .forms import AppointmentForm , ServiceSelectionForm



def HomePages(request):
    return render(request, 'HomePage/hp.html')



def Login(request):
    return render(request, 'account/login.html')


def Register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)  # Create form with POST data
        if form.is_valid():
            # Save the user data to the database after form validation
            form.save()
            # Handle successful registration (e.g., redirect to login page)
    else:
        form = UserRegistrationForm()  # Create an empty form

    context = {'form': form}
    return render(request, 'account/register.html', context)




def index(request):
  """
  Renders the landing page with car wash services.
  """
  services = CarWashService.objects.all()  # Get all services
  context = {'services': services}
  return render(request, 'index.html', context)

def contact(request):
  """
  Handles contact form submission (assuming plain HTML form without forms.py).
  You might want to replace this with a form-based approach in the future.
  """
  if request.method == 'POST':
    # Process contact form data (implement email sending logic here)
    return redirect('index')  # Redirect back to landing page after submission
  return render(request, 'contact.html')  # Render contact form page

def booking(request):
  """
  Handles appointment booking and service selection.
  """
  if request.method == 'POST':
    appointment_form = AppointmentForm(request.POST)
    service_form = ServiceSelectionForm(request.POST)
    if appointment_form.is_valid() and service_form.is_valid():
      # Process valid forms (save appointment data, handle service selections)
      # You'd likely need additional logic to store appointments and selections
      return redirect('success')  # Redirect to success page after booking
  else:
    appointment_form = AppointmentForm()
    service_form = ServiceSelectionForm()
  context = {'appointment_form': appointment_form, 'service_form': service_form}
  return render(request, 'booking.html', context)

def success(request):
  """
  Displays a success message after booking an appointment.
  """
  return render(request, 'success.html')







