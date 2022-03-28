# Fee Files Processor
Um script python para processar arquivos da [FEE](https://dados.fee.tche.br/) em **nível municipal (agregação geográfica municipal)**.

### Instruções:
* Copie o script principal (**script.py**) para o mesmo nível da pasta que contém os dados a serem processados. A cópia pode ser feita através de um git clone de todo o repositório ou o download somente do script via navegador;
* Certifique-se de ter o Python instalado em seu computador, bem como as bibliotecas **pandas** e **numpy**. Caso não tenha o Python instalado, vocẽ pode baixá-lo [aqui](https://www.python.org/downloads/). Quanto às bibliotecas, execute o comando `python -m pip install pandas numpy` em um terminal **após** a instalação do python;
* Execute o script usando o terminal de sua preferência (`python script.py`).

O script terá 2 outputs:
* Uma pasta chamada *data* com todos os arquivos processados em formato .csv;
* Um arquivo chamado ***dataset.csv*** contendo todos os arquivos da pasta *data* já mesclados.

O arquivo ***dataset.csv*** é um *dataframe* com estrutura de dados em painel, onde cada linha representa uma observação de um município em um dado ano e as características (*features*) que foram extraídas dos arquivos processados.
Sugestões e feedbacks sobre o script são bem vindos, bem como a abertura de PRs com melhorias e/ou correções de bugs! :D
