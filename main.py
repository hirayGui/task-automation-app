# Importando bibliotecas
import pyautogui as pg
import time
import pandas as pd
import openpyxl as op

# Entrando no sistema para o cadastro dos produtos
pg.PAUSE = 1
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
## Abrindo navegador
pg.press("win")
pg.write("opera")
pg.press("enter")

pg.write(link)
pg.press("enter")

### Aguardando o sistema carregar
time.sleep(3)

# Fazendo login no sistema
## Preenchendo formulário de login
pg.click(x=705, y=497) 
pg.write("email@email.com")
pg.press("tab")
pg.write("senha@12345")
pg.press("tab")
pg.press("enter")

### Aguardando o sistema carregar
time.sleep(3)

# Abrindo base de dados
## Criando dataframe utilizando o arquivo .csv como base de dados
df = pd.read_csv("produtos.csv", sep=",")
print(df)

# Cadastrando 1 produto
# Repetindo rotina de cadastro de produtos até que a lista acabe