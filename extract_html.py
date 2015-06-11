from bs4 import BeautifulSoup
import requests

amazon = requests.get('http://www.amazon.com/')
s = BeautifulSoup(amazon.text)

product_images = s.find_all(class_= 'product-image')


for product_image in product_images:
    print(product_image.get('alt'))





