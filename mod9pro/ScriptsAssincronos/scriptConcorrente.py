from asyncio import coroutine, get_event_loop
from time import time
import requests
import json

class IngestaoDadosDogs:
    def __init__(self, urls, dir):
        self.urls = urls
        self.dir = dir
    
    @coroutine
    def collect(self):
        start = time()
        loop = get_event_loop()
        scrape_list = [loop.run_in_executor(None, requests.get, url) for url in self.urls]
        for i, scrape in enumerate(scrape_list):
            resp = yield from scrape
            arquive = resp.json()
            print(f'{i+1}: {resp.ok}')
            with open(dir+f'{i+1}_File.json', 'w+') as file:
                json.dump(arquive, file)
        termino = time() - start
        print(f'Fim da Operação: {termino:.2f} s')

# API que busca aleatoriamente imagem de cachorros na internet!
url_list = ['https://dog.ceo/api/breeds/image/random' for n in range(0,10)]
# Diretorio onda ira salvar o arquivo JSON
dir = "C:/Users/BlueShift/Desktop/Gustavo/Gustavo/MentoramaPythonPRO/MentoramaPythonPRO_MOD9/mod9pro/JsonConcorrentes/"

Dados = IngestaoDadosDogs(url_list, dir).collect()
loop = get_event_loop()
loop.run_until_complete(Dados)



