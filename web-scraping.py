from bs4 import BeautifulSoup
import csv
import os
from tqdm import tqdm
import requests
import urllib.request

save_directory = os.path.join('raw', 'van-gogh-dataset')
os.makedirs(save_directory, exist_ok=True)

with open('raw/vgdb_2016.csv') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    next(csv_reader, None)
    for row in tqdm(csv_reader):
        url = row[1]
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        img_attrs = soup.find('img').attrs
        img_src = img_attrs['src']
        img_name = img_attrs['alt'][5:]
        urllib.request.urlretrieve(img_src, os.path.join(save_directory, img_name))
