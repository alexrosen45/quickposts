from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url="/signin")
def home(request):
    return render(request, 'index.html', context={
        'data': [{
            "prompt": "Test",
            "datetime": "friday",
            "details": "Testinfo",
            "status": "Pending"
        }, 
        {
            "prompt": "Test",
            "datetime": "friday",
            "details": "Testinfo",
            "status": "Accepted"
        }]
    })

def landing(request):
    return render(request, 'landing.html', context={})
