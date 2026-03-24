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
        attachment = request.FILES.get('attachment')

        contact_entry = Contact(name=name, email=email, subject=subject, message=message, attachment=attachment)
        contact_entry.save()
        messages.success(request, 'Your message has been sent successfully!')

    return render(request, 'contact.html')