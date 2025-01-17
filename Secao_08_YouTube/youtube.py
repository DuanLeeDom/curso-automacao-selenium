import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

chrome_options = Options()
main_directory = os.path.join(sys.path[0])

# Configura o perfil do Chrome
chrome_options.add_argument("--user-data-dir=" + main_directory + "/chrome_profile")

# Abre uma porta de depuração remota para evitar detecção de automação
chrome_options.add_argument("--remote-debugging-port=9223")
# Mantém o chromeDriver em execução em segundo plano após o término do scripy
chrome_options.add_experimental_option("detach", True)
# Desativa a extensão de automação do Chrome para evitar detecção.
chrome_options.add_experimental_option("useAutomationExtension", False)
# Exclui o switch "enable-automation" para ocutar a automação durante a navegação.
chrome_options.add_experimental_option("excludeSwitches",["enable-automation"])

# Cria o serviço para o ChromeDriver
service = Service(ChromeDriverManager().install())

# Inicializa o driver do Chrome
driver = webdriver.Chrome(service=service, options=chrome_options)

# Espera e navega até o YouTube
wait = WebDriverWait(driver, 60)
driver.maximize_window()
driver.get('https://www.youtube.com')
time.sleep(1)
driver.get('https://studio.youtube.com/channel/UCrQgITPXDfm6mJEThJD-ryA/videos?d=ud')

time.sleep(1)
video_path = main_directory + '/video.mp4'
inputVideo = driver.find_element(By.NAME,'Filedata') # imageUpload = driver.find_element(By.XPATH, '//*[@name="Filedata"]')
inputVideo.send_keys(video_path)

time.sleep(5)
titulo = 'Titulo de teste da minha postagem'
descricao = 'Descrição de teste da minha postagem'

inputTitulo = driver.find_element(By.XPATH, '//*[@aria-label="Add a title that describes your video (type @ to mention a channel)"]')
inputTitulo.clear()
inputTitulo.send_keys(titulo)

inputDescricao = driver.find_element(By.XPATH, '//*[@aria-label="Tell viewers about your video (type @ to mention a channel)"]')
inputDescricao.clear()
inputDescricao.send_keys(descricao)

time.sleep()
Thumbnaill_path = main_directory + '/Thumbnaill'
inputThumbnaill = driver.find_element(By.XPATH, '/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[3]/ytcp-video-thumbnail-editor/div[3]/ytcp-video-custom-still-editor/div/ytcp-thumbnail-uploader/ytcp-thumbnail-editor/div[1]/ytcp-ve/button')
inputThumbnaill.send_keys(Thumbnaill_path)