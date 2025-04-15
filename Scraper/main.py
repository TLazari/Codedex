import requests
from bs4 import BeautifulSoup


headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
  'Accept-Language': 'en-US,en;q=0.5'
 }

def get_product_details(product_url:str) -> dict:
    # Cria um dicionario com a página
    product_details = {}
    
    page = requests.get(product_url, headers=headers)
    soup = BeautifulSoup(page.content, features= 'lxml')

    title = soup.find('h1', attrs={'id': 'heading-product-title'}).get_text().strip()
    price = soup.find('span', attrs={'p': 'price-value'}).get_text().strip()

