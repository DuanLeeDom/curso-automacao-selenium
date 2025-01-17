import time
import os
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service  # Importando o Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By  # Adicionando a importação do By

chrome_options = Options()
main_directory = os.path.join(sys.path[0])

# Usando o Service para o ChromeDriver
chrome_driver_path = ChromeDriverManager().install()
service = Service(chrome_driver_path)  # Criando um objeto Service com o caminho do driver

# Inicializando o WebDriver com 'service' e 'options'
driver = webdriver.Chrome(service=service, options=chrome_options)  # Usando 'service' e 'options' para configurar o driver

# código base tudo que está aqui em cima.
# Abertura do Chrome com Selenium 

time.sleep(2)
driver.get('https://professorporcino.com.br/teste-selenium')
driver.maximize_window()
time.sleep(3)

# classe
elemento = driver.find_element(By.CLASS_NAME, 'information')
# find_element é o primeiro a ser encontrado.
print(elemento)
elemento.send_keys('Esse é meu texto!')
time.sleep(2)
elemento.clear()  # Corrigido: falta de parênteses para chamar o método

# lista de elementos | Busca

# CLASS_NAME
elementos = driver.find_elements(By.CLASS_NAME, 'information')
print(elementos)
elementos[0].send_keys('Este é o 1º elemento da classe information')
elementos[1].send_keys('Este é o 2º elemento da classe information')
time.sleep(2)

# CSS_SELECTOR
inputname = driver.find_element(By.CSS_SELECTOR, '#fname') 
valorinputname = inputname.get_attribute('value')
print(valorinputname)

# ID
time.sleep(2)
inputsobrenome = driver.find_element(By.ID, 'lname')
valorinputname = inputsobrenome.get_attribute('value')
print(valorinputname)

# name newsletter
time.sleep(2)
novidades = driver.find_element(By.NAME, 'newsletter')
novidades.click()

# xpath
time.sleep(2)
checkfeminino = driver.find_element(By.XPATH, '/html/body/form/span[2]/input') # "//input[@value='f']"
checkfeminino.click()

# link text
time.sleep(2)
ancora = driver.find_element(By.LINK_TEXT, 'Página Oficial do Selenium')
ancora.click()
time.sleep(2)

time.sleep(5)