# Bot da Cesta Básica Brasileira

Este projeto utiliza web scraping e ETL para calcular o custo da cesta básica no Brasil com base nos dados do DIEESE e do Atacadão. Os resultados são publicados automaticamente em um bot no Twitter.

## Funcionalidades
- **Web Scraping**:
  - Coleta dados da cesta básica do DIEESE.
  - Extrai preços do Atacadão.
- **ETL Pipeline**:
  - Calcula variação diária e acumulada do mês.
  - Gera relatórios detalhados.
- **Bot no Twitter**:
  - Publica atualizações automáticas com os resultados do dia.

## Como Usar
1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
2. Configure suas credenciais do Twitter no arquivo `twitter_bot.py`.
3. Execute o pipeline:
   ```bash
   python main.py
   ```
4. Os resultados serão publicados automaticamente no Twitter e salvos na pasta `output/`.

## Estrutura do Repositório
- `scraper/`: Scripts para coleta de dados.
- `etl/`: Pipeline de ETL.
- `output/`: Dados processados e relatórios.
- `README.md`: Documentação do projeto.
- `twitter_bot.py`: Script para integração com o Twitter.

## Melhorias Futuras
- Adicionar suporte para mais fontes de dados.
- Melhorar os cálculos de variação percentual.

---
