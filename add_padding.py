import csv
from PIL import Image
import requests
from io import BytesIO
import os

def make_square(im, min_size=256, padding=200, fill_color=(255, 255, 255, 255)):
    x, y = im.size
    size = max(min_size, x + 2 * padding, y + 2 * padding)
    new_im = Image.new('RGBA', (size, size), fill_color)
    new_im.paste(im, (padding + (size - x - 2 * padding) // 2, padding + (size - y - 2 * padding) // 2))
    return new_im

def process_images_from_csv(csv_file_path):
    output_dir = 'images'
    os.makedirs(output_dir, exist_ok=True)

    print(f"Opening CSV file at path: {csv_file_path}")
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        print("CSV reader created successfully, reading rows...")
        for row in reader:
            image_url = row['Изображения']
            print(f"Trying to load image from URL: {image_url}")
            try:
                response = requests.get(image_url)
                response.raise_for_status()
                image = Image.open(BytesIO(response.content))
                image = make_square(image)
                image_path = os.path.join(output_dir, f"processed_{row['Артикул']}.png")
                image.save(image_path)
                print(f"Image saved to {image_path}")
            except requests.exceptions.RequestException as e:
                print(f"Failed to load image from {image_url}: {e}")
            except IOError as e:
                print(f"Failed to process or save image from {image_url}: {e}")

# Укажите путь к вашему CSV файлу
csv_file_path = r'C:\Users\David\Documents\Парсер\Padding Image\Padding Image\tasks\file.csv'
process_images_from_csv(csv_file_path)
