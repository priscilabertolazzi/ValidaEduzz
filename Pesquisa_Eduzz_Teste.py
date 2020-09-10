"""
Este script pesquisa a palavra "Eduzz" no buscador Google no navegador Chrome, e verifica se no resultado www.eduzz.com contém o texto "Vem crescer com a gente."

Dependências:
$ pip install selenium
"""

#importando o módulo webdriver e a classe keys do pacote selenium, e o pacote time
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

class TesteEduzz(): #criando uma classe de testes
    def test_valida_texto(self): #implementando o cenário de teste
        self.driver = webdriver.Chrome(r"C:\chromedriver.exe") #passando o executável do chromedriver instalado na máquina para o selenium se comunicar com o navegador Chrome, o "r" é para o python reconhecer a "\"
        self.driver.set_page_load_timeout(10) #aguarda 10 segundos o navegador Chrome abrir, se exceder esse tempo interrompe o teste
        self.driver.maximize_window() #maximizando a janela do Chrome
        self.driver.get("https://google.com.br") #chamando o endereço do Google
        self.driver.find_element_by_name("q").send_keys("Eduzz") #digitando a palavra Eduzz no campo de busca do Google
        self.driver.find_element_by_name("q").send_keys(Keys.ENTER) #enviando o comando da tecla <Enter> para realizar a pesquisa
        URL = self.driver.find_element_by_css_selector("div:nth-child(2) > .rc:nth-child(2) a .iUh30").text #criando a variável "URL" para guardar o conteúdo do elemento que contém os sites retornados na busca do Google
        titulo = self.driver.find_element_by_css_selector("#rso > div:nth-child(1) > div > div > div.r > a > h3").text #criando a variável "titulo" para guardar o contéudo do elemento que contém os títulos dos sites retornados na busca do Google
        time.sleep(5) #aguardando 5 segundos para fazer o próximo comando
        self.driver.quit() #encerrando o webdriver
        if URL == "www.eduzz.com": #comparando se o conteúdo guardado na variável "URL" é igual ao valor www.eduzz.com
            assert "Vem crescer com a gente." in titulo, "O resultado do site www.eduzz.com não contém o texto \"Vem crescer com a gente.\"" #se for igual valida se o texto "Vem crescer com a gente." está contido na variável "titulo", se não conter o texto na variável "titulo" é exibida a mensagem que o site www.eduzz.com não contém o texto
        else: #se o contéudo da variável "URL" for diferente de www.eduzz.com é exibida a mensagem que o site não foi encontrado na busca
            print("O site www.eduzz.com não foi encontrado na busca.")

if __name__ == "__main__": #condição do python para executar diretamente esse script
        teste = TesteEduzz() #instaciando a classe "Teste_GetPokemon()"
        teste.test_valida_texto() #chamando o método da classe "TesteEduzz()" que valida o cenário de teste