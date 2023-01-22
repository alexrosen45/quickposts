import tweepy
from django.conf import settings


def create_tweet(
        tweet_text: str,
        media_file_name: str,
        TWITTER_API_KEY: str,
        TWITTER_API_SECRET: str,
        TWITTER_ACCESS_TOKEN: str,
        TWITTER_ACCESS_TOKEN_SECRET: str) -> None:
    """Function that creates tweet with media."""

    # Setting up client
    client = tweepy.Client(
        consumer_key=TWITTER_API_KEY,
        consumer_secret=TWITTER_API_SECRET,
        access_token=TWITTER_ACCESS_TOKEN,
        access_token_secret=TWITTER_ACCESS_TOKEN_SECRET
    )

    auth = tweepy.OAuthHandler(
        consumer_key=TWITTER_API_KEY,
        consumer_secret=TWITTER_API_SECRET
    )
    auth.set_access_token(key=TWITTER_ACCESS_TOKEN,
                          secret=TWITTER_ACCESS_TOKEN_SECRET
                          )
    api = tweepy.API(auth)

    # Uploading medias
    media = api.media_upload(filename=media_file_name)

    # Creating tweet
    response = client.create_tweet(text=tweet_text, media_ids=[media.media_id])

    print(response)
