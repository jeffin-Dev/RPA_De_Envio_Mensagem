from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import urllib.parse


class Navegador:
    def __init__(self):
        self.numero = None
        self.mensagem = None
        self.situacao = []
        self.numero_situacao = []

    def enviar_mensagens(self, numeros, mensagem):
        # servico = Service(ChromeDriverManager().install())
        # driver = webdriver.Chrome(service=servico)
        driver = webdriver.Chrome()
        texto = urllib.parse.quote(mensagem)
        # driver.get(f'https://web.whatsapp.com/')
        # while len(driver.find_elements(By.XPATH, '//*[@id="app"]/div/div/div[3]/div[1]/div/div/div[2]/div/canvas')) < 1:
        #     time.sleep(1)
        # time.sleep(1)
        # while len(driver.find_elements(By.XPATH, '//*[@id="app"]/div/div/div[4]/header/div[1]/div/img')) < 1:
        #     time.sleep(1)
        # time.sleep(8)
        for numero in numeros:
            # abrir cvs com a pessoa
            print(f'Abrindo conversa com {numero}')
            driver.get(f'https://api.whatsapp.com/send/?phone=55{numero}&text={texto}&type=phone_number&app_absent=0')
            time.sleep(3)
            # clicar em inciar conversa
            botao_iniciar_conversa = '/html/body/div[1]/div[1]/div[2]/div/section/div/div/div/div[2]/div[1]/a'
            while len(driver.find_elements(By.XPATH, botao_iniciar_conversa)) < 1:
                time.sleep(1)
            time.sleep(2.5)
            driver.find_element(By.XPATH, botao_iniciar_conversa).click()
            # abrir whats web
            botao_abrir_whatsaap_web = '/html/body/div[1]/div[1]/div[2]/div/section/div/div/div/div[3]/div/div/h4[2]/a'
            while len(driver.find_elements(By. XPATH, botao_abrir_whatsaap_web)) < 1:
                time.sleep(1)
            time.sleep(2.5)
            driver.find_element(By.XPATH, botao_abrir_whatsaap_web).click()
            whatsaap_aberto = '//*[@id="app"]/div/div/div[4]/header/div[1]/div/img'
            while len(driver.find_elements(By.XPATH, whatsaap_aberto)) < 1:
                time.sleep(1)
            time.sleep(2)
            try:
                pop_up_carregando = '/html/body/div[1]/div/span[2]/div/span/div/div/div/div'
                while len(driver.find_elements(By.XPATH, pop_up_carregando)) > 0:
                    print('Carregando chat')
                    pop_up_numero_invalido = '/html/body/div[1]/div/span[2]/div/span/div/div/div/div/div/div[1]'
                    if 'url' in driver.find_element(By. XPATH,pop_up_numero_invalido).text:
                        time.sleep(1)
                        break
                    time.sleep(1)
                time.sleep(4)
                botao_enviar = '/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button'
                driver.find_element(By.XPATH,botao_enviar).click()
                print('Mensagem enviada para {}'.format(numero))
                situacao = 'Mensagem Enviada.'
                self.numero_situacao.append(numero)
                self.situacao.append(situacao)
                time.sleep(4)
            except:
                print(f'{numero} não existe')
                situacao = 'Número Inválido.'
                self.numero_situacao.append(numero)
                self.situacao.append(situacao)
                time.sleep(2)
            finally:
                time.sleep(1)

    def pegar_situacao(self):
        return self.situacao


if '__main__' == __name__:

    a= Navegador()
    a.enviar_mensagens(['23364','31973093105','23547'], 'teste')



