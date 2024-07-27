import csv
import requests
import os


# Функция для получения JWT токена
def get_jwt_token(admin, Asdf12321-):
    url = "https://dodoma.softnova.ru/wp-json/jwt-auth/v1/token"
    headers = {"Content-Type": "application/json"}
    data = {"username": admin, "password": Asdf12321-}
    response = requests.post(url, json=data, headers=headers)
    response_data = response.json()
    return response_data["353408ad504294d2969438b2d625f76149917b2332c0d896652a15b1d4b5305a"]


# Функция для обновления изображения товара
def update_product_image(product_id, image_url, 353408ad504294d2969438b2d625f76149917b2332c0d896652a15b1d4b5305a):
    url = f"https://dodoma.softnova.ru/wp-json/wp/v2/products/{product_id}"
    headers = {
        "Authorization": f"Bearer {353408ad504294d2969438b2d625f76149917b2332c0d896652a15b1d4b5305a}",
        "Content-Type": "application/json"
    }
    data = {"image_url": image_url}
    response = requests.post(url, json=data, headers=headers)
    return response.json()


# Чтение CSV файла и обновление изображений товаров
def process_images_from_csv(csv_file_path, token):
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            product_id = row['ID']
            image_url = row['Изображения']
            print(f"Updating product {product_id} with image {image_url}")
            response = update_product_image(product_id, image_url, token)
            print(response)


# Основная функция
def main():
    # Учетные данные администратора WordPress
    username = "your_admin_username"
    password = "your_admin_password"

    # Получение JWT токена
    token = get_jwt_token(username, password)

    # Путь к вашему CSV файлу
    csv_file_path = r'C:\Users\David\Documents\Парсер\Padding Image\Padding Image\tasks\file.csv'

    # Обработка изображений из CSV файла
    process_images_from_csv(csv_file_path, token)


if __name__ == "__main__":
    main()
