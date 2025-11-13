import pyautogui as py
import time

# Pausa de 1s para lentidão (Computadores mais lentos aumentar o tempo)
py.PAUSE = 1

# abrir o navegador (Chrme)
py.press("win")
py.write("chrome")
py.press("enter")

# tempo para carregar o Chrome
time.sleep(5)

# entrar no site
py.write("https://www.hashtagtreinamentos.com/curso-python")
py.press("enter")

# Aguardar um tempo para carregar o site
time.sleep(5)

# coletar os dados 