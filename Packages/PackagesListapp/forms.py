from django import forms
from .models import User , Package
from .models import CarWashService  # Assuming you have models.py

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password']



    class PackageForm(forms.ModelForm):
       class Meta:
        model = Package
        fields = '__all__'  # Display all fields from the model




    class AppointmentForm(forms.Form):
        """
        Form to capture user information for booking a car wash appointment.
        """
        name = forms.CharField(label="Your Name", max_length=100, required=True)
        email = forms.EmailField(label="Your Email", required=True)
        phone_number = forms.CharField(label="Phone Number", max_length=15, required=False)  # Optional phone number
        date = forms.DateField(label="Appointment Date", required=True, widget=forms.SelectDateWidget)  # Date picker
        time = forms.TimeField(label="Appointment Time", required=True)
        # Add a field for selecting services (explained later)
        message = forms.CharField(label="Additional Message", widget=forms.Textarea, required=False)  # Optional message

    class ServiceSelectionForm(forms.Form):
        """
        Form to allow users to select car wash services for their appointment.
        """
        services = forms.MultipleChoiceField(  # Allows selecting multiple services
            label="Select Services",
            choices=[(service.pk, service.name) for service in CarWashService.objects.all()],
            # Dynamic list based on services
            required=True
        )

