from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from posts.models import Post


@login_required(login_url="/signin")
def home(request):
    return render(request, 'index.html', context={
        'data': Post.objects.filter(user=request.user)
    })
