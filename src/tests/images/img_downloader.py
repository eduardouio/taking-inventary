import requests
import os
from tqdm import tqdm
import requests
from bs4 import BeautifulSoup
import json


path_save = os.path.abspath("imgs/")
mess = "Progreso"
ncols = 200

init_report = open("list_urls.txt", "r")
init_report = init_report.read().split("\n")
report = [
    {
        "account_code": itm.split(",")[0],
        "base_url": itm.split(",")[2],
        "url_img": "",
        "file_name": "",
        "file": ""
    }
    for itm in init_report
]

print('Otener urls de imagenes')


def get_image_urls():
    for line_item in tqdm(report, total=len(report), desc=mess, ncols=ncols):
        page_url = line_item["base_url"].strip()
        response = requests.get(page_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        data = soup.find_all('img', {'class': 'wp-post-image'})
        if data:
            img = data.pop()
            if img.attrs.get('data-large_image'):
                url_img = img.attrs.get('data-large_image')
                url_img = url_img.replace('&nocache=1', '')
                line_item['url_img'] = url_img.replace(
                    'https://laguarda.com.ec/wp-content/webpc-passthru.php?src=',
                    ''
                )
            else:
                line_item['url_img'] = ""
        else:
            line_item['url_img'] = ""


print('Descargando imagenes en {}'.format(path_save))


def download_images():
    for url in tqdm(urls, total=len(report), desc=mess, ncols=ncols):
        if url['url_img']:
            response = requests.get(url['url_img'])
            filename = url['url_img'].split('/')[-1]
            with open(path_save + '/' + filename, 'wb') as file:
                file.write(response.content)

            url['file'] = path_save + filename


get_image_urls()
download_images()

file_names = json.dumps(report)
with open('report.json', 'w') as file:
    file.write(file_names)
