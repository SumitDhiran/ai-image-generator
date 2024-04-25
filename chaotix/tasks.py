from celery import shared_task
import base64
import os
import requests
from core.models import ImageData
from dotenv import load_dotenv

load_dotenv()

engine_id = "stable-diffusion-xl-1024-v1-0"
api_host = os.getenv('API_HOST', 'https://api.stability.ai')
api_key = os.getenv("STABILITY_API_KEY")



@shared_task
def generate_image_from_prompt(prompt):
    """
    this function calls the stability.ai API to
    generate a image based on the given prompt

    raises: if prompt is not present
            if api_key is not present
            if response.status_code is not 200
    """
    assert bool(prompt), "prompt can not be empty"

    if api_key is None:
        raise Exception("Missing Stability API key.")

    response = requests.post(
        f"{api_host}/v1/generation/{engine_id}/text-to-image",
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {api_key}"
        },
        json={
            "text_prompts": [
                {
                    "text": f"{prompt}"
                }
            ],
            "cfg_scale": 7,
            "height": 1024,
            "width": 1024,
            "samples": 1,
            "steps": 30,
        },
    )

    if response.status_code != 200:
        raise Exception("Non-200 response: " + str(response.text))

    data = response.json()

    for i, image in enumerate(data["artifacts"]):
        img_data = ImageData.objects.create(
            base64=image["base64"],
            finish_reason=image["finishReason"],
            seed=image["seed"]
        )
        with open(f"./images/out/v1_txt2img_{str(img_data)}.png", "wb") as f:
            f.write(base64.b64decode(image["base64"]))
