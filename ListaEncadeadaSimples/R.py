class Produto:
def __init__(self, codigo•O,
self.codigo • codigo
self.proximo • proximo_nodo
_ _ repr
return '%s %s' % (self.codigo, self.proximo)
class ListaEncadeada:
def _
self.cabeca None
def _repr __(self):
return str(selF.cabeca) • r
def Addñnal(selF,novoCod):
if se If.cabeca:
aux self.cabeca
while(aux.proximo):
aux aux.proximo
aux.proximo Produto(novoCod)
self.cabeca Produto(novoCod)
lista ListaEncadeada()
printCLista vaziar, lista)
print(lista)
Addfinal(lista, 2222)
print(lista)
Addfinal(lista, 2333)
print(lista)