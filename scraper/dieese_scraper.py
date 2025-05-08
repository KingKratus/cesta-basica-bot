import requests
from bs4 import BeautifulSoup

DIEESE_URL = "https://www.dieese.org.br/"

def fetch_dieese_data():
    """
    Coleta dados da cesta básica do site do DIEESE.
    """
    response = requests.get(DIEESE_URL)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Exemplo de como encontrar dados (ajustar seletor conforme necessário)
        data = soup.find_all('table')
        for table in data:
            print(table.text)
    else:
        print("Erro ao acessar o site do DIEESE.")

if __name__ == "__main__":
    fetch_dieese_data()
