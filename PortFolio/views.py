from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
# from .models import Contact

def index(request):
  return render(request,'index.html') #Index.html have the orginal code

@csrf_exempt  # If you are testing without CSRF protection. For production, manage CSRF properly.
def submit_contact_form(request):
    if request.method == 'POST':
        # Retrieve data from the POST request
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Create a new Contact entry in the database
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()

        # Return a JSON response with success message
        return JsonResponse({'status': 'success', 'message': 'Contact form submitted successfully'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)