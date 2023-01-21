from django.shortcuts import render


def home(request):
    if request.method == "POST":
        print(request.POST)
    return render(request, 'index.html')
