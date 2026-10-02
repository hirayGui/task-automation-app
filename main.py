# Importando bibliotecas
import pyautogui as pg
import time
import pandas as pd

# Entrando no sistema para o cadastro dos produtos
pg.PAUSE = 0.5
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
## Preenchendo formulário de cadastro de produto e repetindo rotina de cadastro de produtos até que a lista acabe
for linha in df.index:
    codigo = str(df.loc[linha, "codigo"])
    marca = str(df.loc[linha, "marca"])
    tipo = str(df.loc[linha, "tipo"])
    categoria = str(df.loc[linha, "categoria"])
    preco = str(df.loc[linha, "preco_unitario"])
    custo = str(df.loc[linha, "custo"])
    obs = str(df.loc[linha, "obs"])

    ### Código do produto
    pg.click(x=717, y=347)
    pg.write(codigo)
    pg.press("tab")

    ### Marca do produto
    pg.write(marca)
    pg.press("tab")

    ### Tipo do produto
    pg.write(tipo)
    pg.press("tab")


    pg.write(categoria)
    pg.press("tab")

    ### Preço do produto
    pg.write(preco)
    pg.press("tab")

    ### Custo do produto
    pg.write(custo)
    pg.press("tab")

    ### Observação do produto
    if obs != "nan":
        pg.write(obs)
    pg.press("tab")

    ### Enviando formulário
    pg.press("enter")

    ### Scrollando para o início da página para cadastrar o próximo produto
    pg.scroll(5000)

    ### Aguardando o sistema carregar
    time.sleep(3)

