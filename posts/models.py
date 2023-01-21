from django.db import models
from django.conf import settings
import openai
import json
from django.core.files import File
import os
import urllib
import replicate
import cohere

REPLICATE_API_TOKEN = settings.REPLICATE_API_TOKEN
COHERE_API_TOKEN = settings.COHERE_API_TOKEN


class Post(models.Model):
    prompt = models.CharField(max_length=120)
    response = models.TextField()
    image = models.ImageField(upload_to='images', null=True)
    image_url = models.URLField(null=True)
    # status = models.TextField(default='pending')
    # completed = models.BooleanField(default=False)
    # post_at = models.DateTimeField(blank=True, null=True)
    # generated_at = models.DateTimeField(blank=True, auto_now_add=True)

    def get_response(self):
        openai.organization = "org-l5VLx4gFMCKCSsQLK0KavLsu"
        openai.api_key = settings.OPENAI_API_KEY

        # create prompt
        prompt = f"Write a Twitter post caption about: {self.prompt}."

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=60,
        )

        self.response = json.loads(str(response))['choices'][0]['text']

    def get_image(self):
        # set replicate api token as environment variable
        os.environ["REPLICATE_API_TOKEN"] = settings.REPLICATE_API_TOKEN

        # try to generate image from prompt
        try:
            model = replicate.models.get("stability-ai/stable-diffusion")
            version = model.versions.get(
                "f178fa7a1ae43a9a9af01b833b9d2ecf97b1bcb0acfd2dc5dd04895e042863f1")

            inputs = {
                'prompt': "detailed, 4K, simple, Create an image about: " + self.prompt,
                'negative-prompt': "no words",
                'width': 768,
                'height': 768,
                'prompt_strength': 0.8,
                'num_outputs': 1,
                'num_inference_steps': 50,
                'guidance_scale': 7.5,
                'scheduler': "DPMSolverMultistep",
            }

            self.image_url = version.predict(**inputs)[0]
            result = urllib.urlretrieve(self.image_url)
            self.image.save(
                os.path.basename(self.image_url),
                File(open(result[0]))
            )
        except:
            print("An error occurred while trying to generate an image.")

    def save(self, *args, **kwargs):
        if not self.pk:
            self.get_response()
            self.get_image()
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.prompt
