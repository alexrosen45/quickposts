from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
import cohere
from django.conf import settings
import tweepy
from authentication.models import Profile


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


@login_required(login_url="/signin")
def tweet_post(request):
    if request.method == 'POST':
        user = request.user

        post_id = request.POST['post_id']
        post = Post.objects.get(id=post_id)

        profile = Profile.objects.get(user=user)

        # create tweet
        client = tweepy.Client(
            consumer_key=settings.TWITTER_API_KEY,
            consumer_secret=settings.TWITTER_API_KEY_SECRET,
            access_token=profile.ACCESS_TOKEN,
            access_token_secret=profile.ACCESS_SECRET
        )

        response = client.create_tweet(text=post.response)
        print(response)
        # try:
        #     user = request.user
        #     post_id = request.POST['post_id']
        #     post = Post.objects.get(id=post_id)

        #     # create tweet
        #     client = tweepy.Client(
        #         consumer_key=settings.TWITTER_API_KEY,
        #         consumer_secret=settings.TWITTER_API_SECRET,
        #         access_token=user.ACCESS_TOKEN,
        #         access_token_secret=user.ACCESS_SECRET
        #     )

        #     response = client.create_tweet(text=post.response)
        #     print(response)
        # except:
        #     print("An error occured while posting your tweet.")

    return redirect('/home')
