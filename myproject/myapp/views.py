from django.shortcuts import render
from django.contrib import messages
from .models import Contact

def home(request):
    return render(request, 'home.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact_entry = Contact(name=name, email=email, subject=subject, message=message)
        contact_entry.save()
        messages.success(request, 'Your message has been sent successfully!')

    return render(request, 'contact.html')