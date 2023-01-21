from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post


@login_required(login_url="/signin")
def create_post(request):
    if request.method == 'POST':
        # try:
        #     prompt = request.POST['prompt']
        #     post = Post.objects.create(
        #         prompt=prompt,
        #         response=''  # populated by openai response
        #     )
        #     post.save()
        # except:
        #     print("An error occurred while trying to create a post")
        prompt = request.POST['prompt']
        post = Post.objects.create(
            prompt=prompt,
            response=''  # populated by openai response
        )
        post.save()

    return redirect('/home')
