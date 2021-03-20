from django.shortcuts import render
from .models import ContactInfo

# Create your views here.
def contact(request):
    info = ContactInfo.objects.first()
    return render(request, 'contact/contact.html', {
        'info': info
    })