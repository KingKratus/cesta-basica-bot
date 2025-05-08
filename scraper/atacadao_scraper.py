import requests
from bs4 import BeautifulSoup

ATACADAO_URL = "https://www.atacadao.com.br/"

def fetch_atacadao_prices(region):
    """
    Coleta preços de produtos do Atacadão para uma região específica.
    """
    url = f"{ATACADAO_URL}lojas/{region}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Ajustar o seletor conforme necessário
        products = soup.find_all('div', class_='product')
        for product in products:
            name = product.find('h2').text.strip()
            price = product.find('span', class_='price').text.strip()
            print(f"Produto: {name}, Preço: {price}")
    else:
        print(f"Erro ao acessar a página {url}")

if __name__ == "__main__":
    fetch_atacadao_prices("sao-paulo")
