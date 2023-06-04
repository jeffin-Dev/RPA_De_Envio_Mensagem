from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import urllib.parse


class Navegador:
    def __init__(self):
        self.numero = None
        self.mensagem = None

    def cliquei_no_link(self, numero, mensagem):
        servico = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=servico)
        texto = urllib.parse.quote(mensagem)
        driver.get(f'https://web.whatsapp.com/')

        # esperar gerar qrcode
        while len(driver.find_elements(By.XPATH, '//*[@id="pictures"]/div/div/div[3]/div[1]/div/div/div[2]/div/canvas')) < 1:
            time.sleep(1)

        # esperar carregar whats
        while len(driver.find_elements(By.XPATH, '//*[@id="pictures"]/div/div/div[5]/div/div/div[2]/div[1]/h1')) < 1:
            time.sleep(1)
        time.sleep(7)
        print('WhatsApp logado e carregado com sucesso!\nProxima etapa...')

        # numeros = ['31973093105','31985704347', '31989015177']
        # for numero in numeros:
            # print (numero)


        # -------------------- INICIO DO DESPARO  --------------------

        # abrir cvs com a pessoa
        print(f'Abrindo conversa com (AQUI COLOCAR O NOME DO CLIENTE)')
        driver.get(f'https://api.whatsapp.com/send/?phone=55{numero}&text={texto}&type=phone_number&app_absent=0')
        time.sleep(5)

        # clicar em inciar conversa
        while len(driver.find_elements(By.XPATH,'//*[@id="action-button"]')) < 1:
            time.sleep(1)
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="action-button"]').click()

        # abrir whats web
        while len(driver.find_elements(By. XPATH,'//*[@id="fallback_block"]/div/div/h4[2]/a')) < 1:
            time.sleep(1)
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="fallback_block"]/div/div/h4[2]/a').click()

        # Enviar mensagem
        while len(driver.find_elements(By.XPATH,'//*[@id="main"]/footer/div'
                                                '[1]/div/span[2]/div/div[2]/div[1]/div/div[1]')) < 1:
            time.sleep(1)
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="main"]/footer/div'
                                                '[1]/div/span[2]/div/div[2]/div[1]/div/div[1]').send_keys(Keys.ENTER)
        print('mensagem enviada')
        time.sleep(5)

if '__main__' == __name__:

    a= Navegador()
    a.cliquei_no_link('31973093105','teste')



