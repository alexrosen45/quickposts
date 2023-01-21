# quickposts

Automated caption and image generation for your company's Twitter posts.

## Local Stable Diffusion development setup

#### 1. Install anaconda

#### 2. Install stable diffusion development environment

```bash
git clone https://github.com/CompVis/stable-diffusion
```

#### 3. Download model

Create new directory stable-diffusion\models\ldm\stable-diffusion-v1

Donwload sd-v1-4.ckpt weights from https://huggingface.co/CompVis/stable-diffusion-v-1-4-original

Move downloaded weights to new directory

Rename model file to model.ckpt

#### 3. Finish environment setup

Open up an anaconda terminal in stable-diffusion directory and run:

```bash
conda env create -f environment.yaml
conda activate ldm
```

## Submit prompt

```bash
python scripts/txt2img.py --prompt "<prompt here>" --plms --W 256 --H 256
```
