import asyncio
from PIL import Image, ImageFilter
import os
import time


async def process_image(image_path, output_dir):
    start_time = time.time()
    try:
        with Image.open(image_path) as img:
            img = img.filter(ImageFilter.BLUR)
            output_path = os.path.join(output_dir, os.path.basename(image_path))
            img.save(output_path)
            end_time = time.time()
            duration = end_time - start_time
            print(f'Item salvo {output_path}. Tempo: {duration:.4f}.')
    except Exception as e:
        print(f'Erro ao processar {image_path}: {e}')

async def main_image_processing():
    input_dir = "input_images"
    output_dir = "output_images"
    os.makedirs(output_dir, exist_ok=True)
    images = [os.path.join(input_dir, img) for img in os.listdir(input_dir) if img.endswith(".jpg")]
    await asyncio.gather(*(process_image(img, output_dir) for img in images))

if __name__ == "__main__":
    asyncio.run(main_image_processing())
