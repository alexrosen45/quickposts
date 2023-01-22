# quickposts

Automated caption and image generation for your company's Twitter posts.

## Overview
[Quickposts](https://quickposts.ca/) is a web application that uses StableDiffusion, co:here, and Davinci to generate image and text for automated twitter posts. 
The backend consists of an nginx server configured to reverse-proxy incoming traffic to GUnicorn, which then passes traffic to Django. 
The frontend is a mix of HTML, TailWind CSS, and JavaScript served dynamically from Django. Image files (logos, etc.) are served statically from Nginx. 

To install the repo in a local environment, clone it, move to the project directory, run `pip install -r requirements.txt` and then `python3 manage.py runserver 0.0.0.0:YOURPORT`.

Note that you will need to set up a `.env` environment variable file in the main directory. Specify `OPENAI_API_KEY`, `REPLICATE_API_TOKEN`, `COHERE_API_TOKEN`, `TWITTER_API_KEY`, and `TWITTER_API_KEY` in this file. 

See below for instructions on how to setup Stable Diffusion locally. 

## Local Stable Diffusion development setup

#### 1. Install anaconda

#### 2. Install stable diffusion development environment

```bash
git clone https://github.com/CompVis/stable-diffusion
```

#### 3. Download model

Create new directory stable-diffusion\models\ldm\stable-diffusion-v1

Download sd-v1-4.ckpt weights from https://huggingface.co/CompVis/stable-diffusion-v-1-4-original

Move downloaded weights to new directory

Rename model file to model.ckpt

#### 3. Finish environment setup

Open up an anaconda terminal in stable-diffusion directory and run:

```bash
conda env create -f environment.yaml
conda activate ldm
```

### Submit prompt

```bash
python scripts/txt2img.py --prompt "<prompt here>" --plms --W 256 --H 256
```

## Contact
Questions? Interested in contributing? Submit an issue or pull request on GitHub!
