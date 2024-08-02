import requests

def get_random_cat_image():
    try:
        response = requests.get("https://api.thecatapi.com/v1/images/search")
        response.raise_for_status()  # вызывает исключение для ответов с кодами 4xx, 5xx
        data = response.json()
        return data[0]['url'] if data else None
    except requests.exceptions.HTTPError as http_err:
        return None
    except Exception as err:
        return None