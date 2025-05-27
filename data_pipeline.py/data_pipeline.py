import requests
import numpy as np
import pandas as pd
import logging
import schedule
import time

import warnings
warnings.filterwarnings("ignore")

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

headers = {"chave-api-dados" : "4d9de143210bd25f5dc260fae3afa3ec"}

def run_request(url_):
    resposta = requests.get(url_, headers=headers)
    return resposta.json()

def coletar_dados(url):
    logging.info('Pegou URL para a criação das diferentes URLs criando uma para cada página')
    list_urls = [url + str(i) for i in range(1, 6)]
    arr_urls = np.asarray(list_urls)
    
    vec_run = np.vectorize(run_request)  
    logging.info('Fazendo uma requisição para cada URL')
    arr_responses = vec_run(arr_urls)
    logging.info('Requisições concluídas')
    arr_responses = arr_responses.tolist()
    reposta = np.concatenate(arr_responses).tolist()
    return reposta

def transformar_dado(dado):
    logging.info('Criando dataframe')
    df = pd.DataFrame(dado)

    logging.info('Selecionando colunas')
    df_area = df[['funcao', 'valorEmpenhado']]

    logging.info('Transformando dado string -> float')
    df_area['valorEmpenhado'] = df_area['valorEmpenhado'].str.replace('.', '').str.replace(',', '.').astype(np.float64)

    logging.info('Transformando dado string -> float')
    agg_area = df_area.groupby('funcao').sum('valorEmpenhado')

    logging.info('Transformando dados para retirar proporção em porcentagem')
    agg_area = agg_area['valorEmpenhado']/df_area['valorEmpenhado'].sum()
    agg_area = agg_area.reset_index()
    return agg_area

def carga(dado):
    logging.info('Transformando dados para retirar proporção em porcentagem')
    dado.to_csv('/Users/Administrador/data_pipeline.py/distribuicao_empenho_area_2022.csv', index=True)
    logging.info('Arquivo salvo')
    

def etl():
    logging.info('ETL iniciada...')
    
    url = 'https://api.portaldatransparencia.gov.br/api-de-dados/emendas?ano=2022&pagina='
    dado = coletar_dados(url)
    dado = transformar_dado(dado)
    carga(dado)
    logging.info('ETL finalizada...')


schedule.every().day.at('14:59').do(etl)


while True:
    schedule.run_pending()
    time.sleep(3600)
    print('-----------Rodou novamente-----------')