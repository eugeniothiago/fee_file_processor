# Fee Files Processor
Um script python para processar arquivos da FEE em **nível municipal**.

### Instruções:
* Copie o script principal (**script.py**) para o mesmo nível da pasta que contém os dados a serem processados. A cópia pode ser feita através de um git clone de todo o repositório ou o download somente do script via navegador;
* Certifique-se de ter a biblioteca **pandas** e **numpy** instaladas em sua máquina. Caso tenha dúvidas, execute o comando `python -m pip install pandas numpy` para instalar;
* Renomeie a pasta contendo os arquivos .zip a serem processados para **raw_data**;
* Execute o script usando o terminal de sua preferência (`python script.py`).

O script terá 2 outputs:
* Uma pasta chamada *data* com todos os arquivos processados em .csv;
* E um arquivo chamado ***dataset.csv*** contendo todos os arquivos da pasta data já mesclados.

O arquivo ***dataset.csv*** é um *dataframe* com estrutura de dados em painel, onde cada linha representa uma observação de um município em um dado ano e as características (*features*) que foram baixadas no site da FEE.
Sugestões e feedbacks sobre o script são bem vindos, bem como a abertura de PRs com melhorias e/ou correções de bugs! :D
