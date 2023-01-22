from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from posts.models import Post


@login_required(login_url="/signin")
def home(request):
    return render(request, 'index.html', context={
        'username': request.user.username,
        'email': request.user.email,
        'data': Post.objects.filter(user=request.user)
    })


def landing(request):
    return render(request, 'landing.html', context={})
