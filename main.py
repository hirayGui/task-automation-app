# Importando bibliotecas
import pyautogui as pg
import time

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
# Abrindo base de dados
# Cadastrando 1 produto
# Repetindo rotina de cadastro de produtos até que a lista acabe