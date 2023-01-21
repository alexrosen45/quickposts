from django.db import models
from django.conf import settings
import openai
import json


class Post(models.Model):
    prompt = models.CharField(max_length=120)
    response = models.TextField()
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

    def save(self, *args, **kwargs):
        if not self.pk:
            self.get_response()
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.prompt
