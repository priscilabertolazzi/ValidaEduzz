# ValidaEduzz
> Script de automação que pesquisa a palavra "Eduzz" no buscador Google no navegador Chrome, e verifica se no resultado www.eduzz.com contém o texto "Vem crescer com a gente."

## Um pouco sobre a Eduzz
A Eduzz é uma multiplataforma que aproxima produtores de conteúdos digitais ou físicos e prestadores de serviços, sempre prezando por um bom relacionamento para o cliente e para seu negócio, tendo como foco ajudar Produtores e Afiliados a alcançarem excelentes resultados através de uma tecnologia exclusiva e inovadora.

#### Saiba mais em:
https://www.eduzz.com/

## Pré Requisitos
* Ter o Python 3 instalado na máquina.
* Ter o pip, instalador de pacotes Python, instalado na máquina.
* Importar as bibliotecas usadas no projeto.
* Ter o webdriver instalado na máquina.
* Fazer download do arquivo Pesquisa_Eduzz_Teste.py deste repositório.


## Instalação no Windows

### Instalar o Python
Saiba mais em: https://python.org.br/instalacao-windows/

Download Python: https://www.python.org/downloads/release/python-362

### Instalar o pip
Em versões do Python +3.4 o pip já vem instalado, portanto é recomendado que a versão do Python esteja sempre atualizada.

Se a sua versão for anterior à essa, veja como instalar o pip em: https://pip.pypa.io/en/stable/installing/

Para mais informações do pip acesse: https://pypi.org/project/pip/

### Instalar o PyCharm (opcional)
O PyCharm é uma IDE que auxilia o desenvolvimento em Python.

Saiba mais em: https://www.jetbrains.com/pt-br/pycharm/

Download PyCharm: https://www.jetbrains.com/pt-br/pycharm/download/

### Instalar as bibliotecas usadas no projeto
Através do Command Prompt (cmd) do Windows você pode instalar as seguintes bibliotecas necessárias para executar o projeto.
Maiores informações acesse o site https://pypi.org/.

* Biblioteca ``selenium``
```sh
pip install selenium
```

* Biblioteca ``seleniumbase``
```sh
pip install seleniumbase
```

Observação: Você pode adicionar essas bibliotecas através do próprio PyCharm caso você esteja utilizando-o.

### Instalar o webdriver
Através do Command Prompt (cmd) do Windows você pode instalar o webdriver do navegador Chrome.

```sh
seleniumbase install chromedriver
```

Para utilizar no PyCharm você pode fazer o download do chromedriver na seguinte página selecionando a opção de acordo com a sua versão do navegador Chrome: https://chromedriver.chromium.org/downloads.

Na linha 15 do arquivo Pesquisa_Eduzz_Teste.py é preciso indicar qual o caminho absoluto da instalação do chromedriver na máquina para o script ser executado com sucesso.

```sh
self.driver = webdriver.Chrome(r"C:\chromedriver.exe")
```

Observação: Os testes foram realizados no navegador Chrome, portanto foi utilizado o chromedriver. 
Para cada navegador é utilizado um webdriver diferente para executar a automação. Sendo eles: chromedriver para o Chrome, edgedriver para o Edge, geckodriver para o Firefox, operadriver para o Opera, e iedriver para o Internet Explorer.

## Execução
Para executar esse projeto utilize o arquivo Pesquisa_Eduzz_Teste.py através do Command Prompt (cmd) do Windows, ou diretamente através do PyCharm.
