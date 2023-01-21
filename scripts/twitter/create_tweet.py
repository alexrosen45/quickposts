import tweepy   
import config

# Setting up client
client = tweepy.Client(consumer_key=config.API_KEY,
                       consumer_secret=config.API_SECRET,
                       access_token=config.ACCESS_TOKEN,
                       access_token_secret=config.ACCESS_TOKEN_SECRET)

auth = tweepy.OAuthHandler(
    consumer_key=config.API_KEY,
    consumer_secret=config.API_SECRET
    )
auth.set_access_token(key=config.ACCESS_TOKEN, 
                      secret=config.ACCESS_TOKEN_SECRET
                      )
api = tweepy.API(auth)

# Uploading medias
media = api.media_upload(filename='Enter image file name here')

# Creating tweet
response = client.create_tweet(text='Enter tweet here', media_ids=[media.media_id])

print(response)