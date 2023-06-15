from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import urllib.parse


class Navegador:
    def __init__(self):
        self.numero = None
        self.mensagem = None

    def enviar_mensagens(self, numeros, mensagem):
        servico = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=servico)
        texto = urllib.parse.quote(mensagem)
        # driver.get(f'https://web.whatsapp.com/')
        #
        # # esperar gerar qrcode
        # while len(driver.find_elements(By.XPATH, '//*[@id="pictures"]/div/div/div[3]/div[1]/div/div/div[2]/div/canvas')) < 1:
        #     time.sleep(1)
        #
        # # esperar carregar whats
        # while len(driver.find_elements(By.XPATH, '//*[@id="pictures"]/div/div/div[5]/div/div/div[2]/div[1]/h1')) < 1:
        #     time.sleep(1)
        # time.sleep(7)
        # print('WhatsApp logado e carregado com sucesso!\nProxima etapa...')

        # numeros = ['']
        for numero in numeros:

            print ('Enviando para o número: {}'.format(numero))
            # -------------------- INICIO DO DESPARO  --------------------
            # abrir cvs com a pessoa
            print(f'Abrindo conversa com {numero}')
            driver.get(f'https://api.whatsapp.com/send/?phone=55{numero}&text={texto}&type=phone_number&app_absent=0')
            # clicar em inciar conversa
            while len(driver.find_elements(By.XPATH,'//*[@id="action-button"]')) < 1:
                time.sleep(1)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="action-button"]').click()
            print('Passei 1')

            # abrir whats web
            while len(driver.find_elements(By. XPATH,'//*[@id="fallback_block"]/div/div/h4[2]/a')) < 1:
                time.sleep(1)
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="fallback_block"]/div/div/h4[2]/a').click()
            print('Passei 2')

            # Enviar mensagem
            while len(driver.find_elements(By.XPATH,'//*[@id="app"]/div/span[2]/div/'
                                                    'span/div/div/div/div/div/div[1]')) < 1:
                time.sleep(1)
            time.sleep(1)

            elemento = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/span[2]/div/span/div/div/div/div')))
            time.sleep(2)
            if elemento:
                driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/span[2]/div/span/div/div/div/div/div/div[2]/div').click()
                continue

            while len(driver.find_elements(By.XPATH,'//*[@id="main"]/footer/div'
                                                    '[1]/div/span[2]/div/div[2]/div[1]/div/div[1]')) < 1:
                time.sleep(1)

            driver.find_element(By.XPATH, '//*[@id="main"]/footer/div'
                                                    '[1]/div/span[2]/div/div[2]/div[1]/div/div[1]').send_keys(Keys.ENTER)
            print(f'Mensagem enviada para {numero}')
            time.sleep(3)


if '__main__' == __name__:

    a= Navegador()
    a.enviar_mensagens(['319730931055, 31973093105'], 'teste')



