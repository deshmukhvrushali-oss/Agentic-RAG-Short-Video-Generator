import os
import requests

def download_images(topic):
    os.makedirs("assets/images", exist_ok=True)

    for i in range(1, 6):

        url = f"https://picsum.photos/1080/1920?random={i}"

        response = requests.get(url)

        with open(f"assets/images/image{i}.jpg", "wb") as f:
            f.write(response.content)

    print("Images Downloaded Successfully")