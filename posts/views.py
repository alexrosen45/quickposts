from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
import cohere
from django.conf import settings


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

        # limit size of prompt using cohere
        if 256 <= len(prompt):
            co = cohere.Client(settings.COHERE_API_TOKEN)

            prompt = co.generate(
                model='xlarge',
                prompt=prompt,
                max_tokens=256,
                temperature=0.6,
                stop_sequences=["--"]
            )[0].text

        # create post
        post = Post.objects.create(
            user=request.user,
            prompt=prompt,
            response=''  # populated by openai response
        )
        post.save()

    return redirect('/home')
