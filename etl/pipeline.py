import pandas as pd
import json

def calculate_daily_variation(data):
    """
    Calcula a variação diária com base nos preços do dia anterior.
    """
    data['daily_variation'] = data['price'].diff()
    data['daily_percentage'] = (data['daily_variation'] / data['price'].shift(1)) * 100
    return data

def calculate_monthly_accumulated(data):
    """
    Calcula o acumulado do mês com base na variação diária.
    """
    data['monthly_accumulated'] = data['daily_variation'].cumsum()
    data['monthly_percentage'] = (data['monthly_accumulated'] / data['price'].iloc[0]) * 100  # Base na primeira entrada do mês
    return data

def load_cesta_basica_data(json_path):
    """
    Carrega os dados da cesta básica a partir de um arquivo JSON.
    """
    with open(json_path, 'r') as file:
        cesta_data = json.load(file)
    return cesta_data

def process_data(new_data, historical_data=None):
    """
    Processa os dados para calcular variação diária e acumulado do mês.
    """
    if historical_data is not None:
        combined_data = pd.concat([historical_data, new_data])
    else:
        combined_data = new_data

    combined_data['date'] = pd.to_datetime(combined_data['date'])
    combined_data = combined_data.sort_values('date')

    combined_data = calculate_daily_variation(combined_data)
    combined_data = calculate_monthly_accumulated(combined_data)

    return combined_data

def save_to_csv(data, output_path):
    """
    Salva os dados processados em um arquivo CSV.
    """
    data.to_csv(output_path, index=False)
    print(f"Dados salvos em {output_path}")

if __name__ == "__main__":
    # Exemplo de dados novos de preços (esses valores seriam derivados do scraping ou entrada manual)
    new_data = pd.DataFrame({
        "date": ["2025-05-07", "2025-05-08"],
        "item": ["cesta_basica", "cesta_basica"],
        "price": [750.00, 755.00]
    })
    historical_data = pd.DataFrame({
        "date": ["2025-05-06"],
        "item": ["cesta_basica"],
        "price": [745.00]
    })

    # Carrega os dados de itens da cesta básica (caso precise calcular custo total com base em preço unitário)
    cesta_basica = load_cesta_basica_data('data/cesta_basica_nacional.json')
    # Aqui você pode processar a cesta_basica para calcular, por exemplo, o custo total da cesta
    # Exemplo: soma de quantidades (a conversão depende de ter preço unitário)
    # total_itens = sum(item['quantidade'] for item in cesta_basica['itens'])
    # print("Total de itens:", total_itens)

    processed_data = process_data(new_data, historical_data)
    save_to_csv(processed_data, "output/cesta_basica.csv") 
