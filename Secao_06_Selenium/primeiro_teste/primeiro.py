# Bibliotecas
import time  # Usada para pausar a execução para que o Selenium possa trocar de páginas
import os  # Para operações relacionadas ao sistema operacional
import sys  # Para manipulação de variáveis e funções do sistema
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.chrome.service import Service # versão 4 não 3

options = Options() # criando um objeto de Options
main_directory = os.path.join(sys.path[0]) # pegando o caminho atual
driver_path = ChromeDriverManager().install() # e instalando o webdriver

service = Service(executable_path=driver_path) # versão 4 não 3
driver = webdriver.Chrome(service=service, options=options) # versão 4 não 3


driver.get("https://www.selenium.dev") # abre um url
time.sleep(2)
driver.get("https://professorporcino.com.br/")
time.sleep(2)
driver.back() # volta para pagina anterior
time.sleep(2)
driver.forward() # avança pra pagina posterior
time.sleep(2)
driver.refresh()
time.sleep(2)