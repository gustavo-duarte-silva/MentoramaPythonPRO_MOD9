from multiprocessing import Queue
from requests import get
from time import time
from bs4 import BeautifulSoup
import codecs

class WebSitesTitles:
    def __init__(self, urls, dir):
        self.urls = urls
        self.dir = dir
        self.inicio = time()
    
    def collect(self):
        titles_list = []
        fila = Queue()
        [fila.put(n) for n in self.urls] 
        while not fila.empty():
            resposta = get(fila.get())
            tags = BeautifulSoup(resposta.text)
            titles = tags.find('title').text
            titles_list.append(titles)
            print(titles)
            print(f'Obitido: {resposta.ok}')
            print('---'*10)
        with codecs.open(dir+'TitlesObtidos.txt', 'w+', "utf-8") as f:
            f.write('Titulos Obtidos:')
            f.write('\n')
            for line in titles_list:
                f.write(f'# {line}')
                f.write('\n')
        termino = time()
        fim = termino - self.inicio
        print(f"Fim da Operação - {fim:.2f} s")


dir = "C:/Users/BlueShift/Desktop/Gustavo/Gustavo/MentoramaPythonPRO/MentoramaPythonPRO_MOD9/mod9pro/ArchieveParaleloTitles/"
urls = [
    'https://www.revistabula.com/12049-ao-10-maiores-super-herois-dos-quadrinhos/',
    'https://azure.microsoft.com/pt-br/services/machine-learning/#product-overview',
    'https://www.rockstargames.com/br/gta-v',
    'https://www.mancity.com/',
    'https://pt.wikipedia.org/wiki/Batman',
    'https://www.python.org/',
    'https://elderscrolls.bethesda.net/pt/',
    'https://spark.apache.org/docs/latest/api/python/',
    'https://pt.wikipedia.org/wiki/SQL',
    'https://ge.globo.com/motor/formula-1/']

WebSitesTitles(urls, dir).collect()