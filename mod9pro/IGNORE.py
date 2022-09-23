#Script da Aula de Paralelo
from multiprocessing import Queue

fila = Queue()
[fila.put(n) for n in [10,5,7,8,2,5,9]] 

while not fila.empty():
    print(fila.get())
    print(['https://randomuser.me/api/' for i in range(0,10)])
