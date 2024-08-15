import pandas as pd
import requests
import time


# Carregar o arquivo csv
df = pd.read_csv(r'C:\Files\BASE LATITUDE LONGITUDE\CEP.csv')

# Criar um dataframe vazio para armazenar os resultados
result_df = pd.DataFrame()

# Iterar sobre cada CEP no dataframe
for cep in df['CEP']:
    time.sleep(2)
    # Fazer a requisição para a API
    response = requests.get(f'https://cep.awesomeapi.com.br/json/{cep}')
    
    # Verificar se a requisição foi bem sucedida
    if response.status_code == 200:
        # Converter a resposta JSON em um dataframe
        data = pd.json_normalize(response.json())

        print(f"recebendo {data}")
        
        # Adicionar o dataframe de dados ao dataframe de resultados
        result_df = pd.concat([result_df, data])
print("Salvando Arquivo")
# Salvar o dataframe de resultados em um arquivo csv
result_df.to_csv(r'C:\Files\BASE LATITUDE LONGITUDE\LOGRADOUROS_MG.csv', sep=';', index=False)

print("Concluído!")
