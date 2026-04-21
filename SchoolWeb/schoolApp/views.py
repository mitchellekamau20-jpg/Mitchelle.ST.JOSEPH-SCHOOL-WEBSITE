from django.shortcuts import render

# Create your views here.
def home(request):
         context = {} # dict that will hold out data
         return render(request, 'schoolApp/home.html', context)
     
def about(request):
            context = {} # dict that will hold out data
            return render(request, 'schoolApp/about.html', context)

def contact(request):
            context = {} # dict that will hold out data
            return render(request, 'schoolApp/contact.html', context)

def admission(request):
            context = {} # dict that will hold out data
            return render(request, 'schoolApp/admission.html', context)

def academics(request):
            context = {} # dict that will hold out data
            return render(request, 'schoolApp/academics.html', context)