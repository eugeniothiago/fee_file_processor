import pandas as pd
import numpy as np
import re
import os
from pathlib import Path
import gc
from zipfile import ZipFile
from unidecode import unidecode
import time
import sys
import posixpath

project_dir = Path("script.py").resolve().parents[0]

print('Iniciando o script')


index_list=[]
folder_list = os.listdir(project_dir)

for idx,folder in enumerate(folder_list):
    folder, ext = os.path.splitext(folder)
    if ext=='':
        print(f'{idx} - {folder}')
        index_list.append(str(idx))
    pass

user_input = input('Por favor, digite o número correspondente à pasta contendo os dados brutos:')

while user_input not in index_list:
    while not user_input.isdigit():
        user_input = input('Caractere informado não é um dígito. Por favor, digite o número correspondente à pasta contendo os dados brutos:')
        if not user_input.isdigit():
            print('Caractere inserido não é um número. Digite novamente')
    user_input = input('Digito informado não corresponde a uma pasta listada. Por favor, digite o número correspondente à pasta contendo os dados brutos:')

folder = f'{project_dir}/{folder_list[int(user_input)]}'

# lẽ todos os arquivos .zip e descompacta na pasta raw_data:
print(f'Descompactando os arquivos .zip contidos na pasta {folder}:')
raw_data_list = [data for data in os.listdir(folder)]

if not os.path.exists('fee_data'):
    os.mkdir('fee_data')
        
for archive in raw_data_list:
    if not raw_data_list:
        print('Não há nenhum arquivo .zip na pasta raw_data. O script será encerrado.')
        sys.exit()
    else:
        name, extension = os.path.splitext(archive)
        if extension =='.zip':
            with ZipFile(f'{folder}/{archive}','r') as zipfile:
                zipfile.extractall(f'{project_dir}/fee_data/')
del archive, name, extension, raw_data_list
gc.collect()


print('Descompactação concluída. Tratando os dados...')

if not os.path.exists('fee_melted_data'):
        os.mkdir('fee_melted_data')

#expandindo e formatando os arquivos que foram compactados:
for file in os.listdir(f'{project_dir}/fee_data/'):
    data = pd.read_csv(f'{project_dir}/fee_data/{file}',sep='\n', encoding='latin-1', header=None)
    data = data[0].str.split(';', expand=True)
    data = data.reset_index(drop=True)
    var_name = data[0][1][7:]
    var_name = unidecode(var_name).lower().strip().replace(' ','_').replace('/','_').replace(':','')
    data.columns = data.iloc[5].tolist()
    data = data.drop([0,1,2,3,4,5], axis=0).reset_index(drop=True)
    data = data.drop(columns=['latitude','longitude'])
    for column in data.columns[2:]:
        column_name = re.sub(r'\D*','',column)
        data = data.rename(columns={column:f'{column_name}'})
    
    data_melted = data.melt(id_vars=['Município','ibge'], var_name=f'ano', value_name=f'{var_name}_value')
    data_melted.to_csv(f'{project_dir}/fee_melted_data/{var_name}_value.csv', sep=';', decimal=',', encoding='latin-1', index=False)
del data, data_melted, file, var_name
gc.collect()

#criando o dataset inicial e realizando o merge com os dados disponíveis
file_list = [file for file in os.listdir(f'{project_dir}/fee_melted_data/')]
melted_data = pd.read_csv(f'{project_dir}/fee_melted_data/{file_list[0]}', header=0, sep=';',encoding='latin-1')
#melted_data.columns = melted_data.iloc[0]
#melted_data = melted_data.drop([0], axis=0)
melted_data = melted_data.astype({'ibge':'str','ano':'str'})

for file in file_list[1:]:
    df= pd.read_csv(f'{project_dir}/fee_melted_data/{file}', header=0, sep=';', encoding='latin-1')
    #df.columns = df.iloc[0]
    #df = df.drop([0], axis=0)
    df = df.astype({'ibge':'str','ano':'str'})
    df = df.sort_values(['Município','ano'])
    melted_data = melted_data.merge(df, on=['Município','ibge','ano'], suffixes=('','_D'), how='outer')
    melted_data = melted_data.drop(melted_data.filter(regex='_D$').columns.tolist(), axis=1)

melted_data.to_csv(f'{project_dir}/dataset.csv', sep=';',decimal=',', encoding='latin-1')

print('Processamento concluído. Os dados em painel estão disponíveis no arquivo dataset.csv!')
