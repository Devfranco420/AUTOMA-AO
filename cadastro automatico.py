#(passo 1) importar bibliotecas
import pyautogui
import time
import pandas

#PAUSE (para o codigo nao rodar muito rapido e dar algum erro)
pyautogui.PAUSE = 0.5

#(passo 2) abrir o google
  #(A): apertar a tecla windows
pyautogui.press('win')
  #(B): escrever google
pyautogui.write('google')
  #(C): apertar enter
pyautogui.press('enter')
  #(D): no meu caso a tela do navegador (google) esta abrindo minimizada, entao preciso maximixar ela
pyautogui.click(x=1241, y=67)
#(passo 3) entrar no site (sistema da empresa) https://dlp.hashtagtreinamentos.com/python/intensivao/login
  #(A): digitar URL
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
  #(B): apertar enter
pyautogui.press('enter')
  #(C): no caso ja estou logado entao e so apertar tab e enter pra logar
pyautogui.click(x=519, y=411)
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('enter')
# respira
time.sleep(3)
#4 IMPORTAR O BANCO DE DADOS (NOSSA TABELA)
tabela = pandas.read_csv('produtos.csv')

print(tabela)

for linha in tabela.index:
  #5 cadastrar o primeiro produto
  pyautogui.click(x=499, y=294)
  codigo = tabela.loc[linha,'codigo']
  pyautogui.write(str(codigo))
  # proximo campo (Marca do produto)
  pyautogui.press('tab')
  marca = tabela.loc[linha, 'marca']
  pyautogui.write(str(marca))
  #proximo (Tipo do produto)
  pyautogui.press('tab')
  tipo_prod = tabela.loc[linha,'tipo']
  pyautogui.write(str(tipo_prod))
  #proximo (Categoria do produto)
  pyautogui.press('tab')
  categoria = tabela.loc[linha,'categoria']
  pyautogui.write(str(categoria))
  pyautogui.press('tab')
  #proximo (Preço unitario do produto)
  preco_unit = tabela.loc[linha,'preco_unitario']
  pyautogui.write(str(preco_unit))
  #proximo (Custo do produto)
  pyautogui.press('tab')
  custo = tabela.loc[linha,'custo']
  pyautogui.write(str(custo))
  #proximo (obs)
  pyautogui.press('tab')
  obs = tabela.loc[linha,'obs']
  if not pandas.isna(obs):
      pyautogui.write(str(tabela.loc[linha, "obs"]))
    #se nao tiver nada      
  pyautogui.press("tab")
  pyautogui.press("enter")
#subir a tela
  pyautogui.scroll(5000)
    
  