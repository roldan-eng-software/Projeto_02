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

# Preencher o formulário
py.click(x=276, y=484)
py.write("Roldan")
py.press("tab")
py.write("roldan.eng.softaware@gmail.com")
py.press('tab')
py.write("16992406202")
py.press('tab')

# Enviar o formulário
py.press('enter')

# Aguardar um tempo para carregar a pagina
time.sleep(5)

# Voltar para o terminal
py.hotkey("alt", "tab")
print('Automação finalizada!')