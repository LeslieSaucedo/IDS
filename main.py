class Nodo:
  def __init__(self,valor,profundidad,padre,hijos):
    self.valor=valor
    self.profundidad=profundidad
    self.padre=padre
    self.hijos=hijos

'''creacion del arbol'''
raiz = Nodo('A',0,None,[])

aux = Nodo('B',1,raiz,[])
raiz.hijos.append(aux)

aux = Nodo('C',1,raiz,[])
raiz.hijos.append(aux)

aux=Nodo('D',2,raiz.hijos[0],[])
raiz.hijos[0].hijos.append(aux)
aux=Nodo('E',2,raiz.hijos[0],[])
raiz.hijos[0].hijos.append(aux)
aux=Nodo('F',2,raiz.hijos[0],[])
raiz.hijos[0].hijos.append(aux)

aux = Nodo('I',3,[raiz.hijos[0].hijos[1],raiz.hijos[0].hijos[2]],[])
raiz.hijos[0].hijos[1].hijos.append(aux)
raiz.hijos[0].hijos[2].hijos.append(aux)

aux = Nodo('G',2,raiz.hijos[1],[])
raiz.hijos[1].hijos.append(aux);
aux = Nodo('H',2,raiz.hijos[1],[])
raiz.hijos[1].hijos.append(aux);

aux = Nodo('J',3,raiz.hijos[1].hijos[0],[])
raiz.hijos[1].hijos[0].hijos.append(aux);
aux = Nodo('K',3,raiz.hijos[1].hijos[1],[])
raiz.hijos[1].hijos[1].hijos.append(aux);

aux = Nodo('L',4,raiz.hijos[1].hijos[0].hijos[0],[])
raiz.hijos[1].hijos[0].hijos[0].hijos.append(aux);
aux = Nodo('M',4,raiz.hijos[1].hijos[0].hijos[0],[])
raiz.hijos[1].hijos[0].hijos[0].hijos.append(aux);

def BusquedaIterativa(nodo, obj, lim):
  if(nodo.valor != obj):
    if(len(nodo.hijos)>0 and nodo.profundidad+1<=lim):
      for i in nodo.hijos:
        nodo = BusquedaIterativa(i, obj, lim)
        if(nodo.valor == obj):
          break
  return nodo

def EncontrarRuta(nodo):
  if(nodo != raiz):
    print(nodo.valor," <- ", end = ""),
    EncontrarRuta(nodo.padre)
  else:
    print(raiz.valor)

objetivo = "E"
aux = BusquedaIterativa(raiz,objetivo,3)
if(aux.valor==objetivo):
  print("Encontrado", aux.valor ,"en la profundidad ",aux.profundidad,)
  EncontrarRuta(aux)
else:
  print("No se encontro "+objetivo)