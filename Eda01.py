import networkx as nx
import math as mt
import matplotlib.pyplot as plt

#################################################################################################################################################################################
########################################################### FUNCIONES Y CLASES PRINCIPALES ######################################################################################
#################################################################################################################################################################################


class City:#Clase ciudad que contiene su nombre,posicion en X y posisicion en Y
  
  def __init__(self, name,posX,posY):
      self.name=name
      self.posX=posX
      self.posY=posY
  
def Distance(NodeA,NodeB): #Calcula la distancia entre nodoA y nodoB
  
  x1=NodeA.posX
  x2=NodeB.posX
  y1=NodeA.posY
  y2=NodeB.posY
  Distance = mt.sqrt( (x2-x1)**2 + (y2-y1)**2 )
  
  return Distance

def NewNode(Map,City): #Agrega 1 nodo sin conexiones al mapa
  
  Map.add_node(City,pos=(City.posX,City.posY))

  return None

def Edges(Map,NodeA,Neighboorhood): #Dado 2 nodos crea una conexion entre ellos en el mapa

  large= len(Neighboorhood)

  for x in range(large):
    Map.add_edge(NodeA,Neighboorhood[x], weight=Distance(NodeA,Neighboorhood[x]))

  return None

def Path_greed(Map,Ini,End,LDist,EdgeList): #Lista que retorna el camino entre ciudad A y ciudad B utilizando greed(siempre elegir el camino mas corto), y retorna la distancia total recorrida
  
  Current=Ini
  Path=list()
  Path.append(Current)
  DistanceT=0
  Edge=None
  Next=None

  while True:
    
    if Current==End:
      break

    Neighbors=list(Map.neighbors(Current))  #Lista con los nodos Vecinos de un NodoA
    Dtn=9999999

    for x in range(len(Neighbors)):

      weight=Map.edges[Current,Neighbors[x]]['weight']
      
      if weight<Dtn and Neighbors[x] not in Path: #Se cumple la condicion si el camino es mas corto que el anterior y no esta en la lista de nodos ya visitados
        Dtn=weight
        Next=Neighbors[x] #Guarda el nodo Vecino si se cumplen las condicioens
        Edge=(Current,Neighbors[x]) #Guarda el camino entre nodoA y nodoB adyacente a el

    DistanceT+=Dtn
    EdgeList.append(Edge)
    Path.append(Next)
    Current=Next

  LDist.append(DistanceT)

  return Path 

def NodesName(L):#Dibuja en el grafico los nombres de los nodos

  labels={}

  for x in range(len(L)):

    labels[L[x]]=r"$"+L[x].name+"$"

  return labels

def Draw(Map,pos,Path,Edges):#Dibuja los nodos con sus conexiones y posiciones respectiva en la ventana de graficos(tambien dibuja el camino recorrido dependiendo de la funcion
                            #que se le dee
  
  NodeColors= ["orchid" if Node in Path else "lime" for Node in Map.nodes()] #COLOREA LOS NODOS de color que cumplen la condicion
  EdgeColors= ["red" if Edge in Edges else "cyan" for Edge in Map.edges()] #Colorea los caminos , que cumplen la condicion
  nx.draw_networkx_nodes(Map, pos=pos, node_color=NodeColors) #
  nx.draw_networkx_edges(Map, pos=pos, edge_color=EdgeColors) #edge_color # color de las conexionesds

  return None

def pushback(L,nombre,posX,posY,Map):
  
  Current=City(nombre,posX,posY)
  L.append(Current)
  NewNode(Map,Current)

  return None
  
def SearchAst(Map,Ini,End,LDist,EdgeList): #Busca el camino mas corto entre Current y End utilizando el algoritmo SearchA*(heuristica greedy+mejor nodo mas corto)
  
  Current=Ini
  Path=list()
  Path.append(Current)
  Trayecto=0
  Edge=None
  Next=None

  while True:
    
    if Current==End:
      break

    Neighbors=list(Map.neighbors(Current))  #Lista con los nodos Vecinos de un NodoA
    Dtn=9999999

    for x in range(len(Neighbors)):

      weight=Map.edges[Current,Neighbors[x]]['weight']
      KNext=weight+Distance(End,Neighbors[x])
      

      
      if KNext<=Dtn and Neighbors[x] not in Path: #Se cumple la condicion si el camino es mas corto que el anterior y no esta en la lista de nodos ya visitados
        Dtn=weight
        Next=Neighbors[x] #Guarda el nodo Vecino si se cumplen las condicioens
        Edge=(Current,Neighbors[x]) #Guarda el camino entre nodoA y nodoB adyacente a el
        EdgeW=(Neighbors[x],Current)
        
    Current=Next    
    Trayecto+=Dtn
    EdgeList.append(Edge)
    EdgeList.append(EdgeW)
    Path.append(Current)
    

  LDist.append(Trayecto)

  return Path 


#################################################################################################################################################################################
############################################################## Funciones Poblar Mapa Predefiniodas ##############################################################################
#################################################################################################################################################################################


def ListCity (Map):#Ciudades en el mapa predefinidas en el codigo para testear (sin input de usuario para testeo) #Retorna una lista con todos los nodos
  L=list()

  pushback(L,"Santiago",152,105,Map) #X
  pushback(L,"Valparaiso",20,130,Map) #x
  pushback(L,"San Antonio",20,20,Map) #x 
  pushback(L,"Villa Alemana",55,130,Map) #x
  pushback(L,"Melipilla",90,5,Map)# x
  pushback(L,"Con con",32,160,Map)# X
  pushback(L,"Quilpue",44,130,Map)#X
  pushback(L,"Quillota",65,165,Map)#X
  pushback(L,"Quintero",34,180,Map)#X
  pushback(L,"Algarrobo",18,70,Map)#X
  pushback(L,"Casa Blanca",45,77,Map)#X
  pushback(L,"Curacavi",90,60,Map)#x
  pushback(L,"Puchuncavi",40,200,Map)#X
  pushback(L,"Maintencillo",41,220,Map)#x
  pushback(L,"Nogales",65,190,Map)#X
  pushback(L,"Catapilco",60,235,Map)#X
  pushback(L,"La Calera",67,175,Map)#X
  pushback(L,"Llay Llay",120,165,Map)#X
  pushback(L,"San Felipe",150,175,Map)#X
  pushback(L,"Los Andes",160,160,Map)#x
  pushback(L,"Calle Larga",155,145,Map)#x
  pushback(L,"La Cumbre",140,157,Map)#x
  pushback(L,"Rungue",140,140,Map)#x
  pushback(L,"El Tabo",20,50,Map)#x
  pushback(L,"Vina Del Mar",30,135,Map)#X
  pushback(L,"Penaflor",130,30,Map)#X
  pushback(L,"El Monte",110,10,Map)#X
  pushback(L,"Lolenco",110,60,Map)#X 
  pushback(L,"Cartagena",23,25,Map)#X
  pushback(L,"Leyda",50,30,Map)#X
  pushback(L,"Puangue",60,20,Map)#X
  pushback(L,"Lo Orozco",40,90,Map)#X
  pushback(L,"Placilla",35,105,Map)#X
  pushback(L,"Las Rosas",80,62,Map)#X   

  return L

def ListEdges(L):#Conexiones de ciudades predefinidas en el codigo para testear (sin input de usuario para testeo) #SE CAE CON NODOS VACIOS O SUMIDEROS

  #################################################################################################################################################################################
  ############################################################################ DEFINICIONES #######################################################################################
  #################################################################################################################################################################################

  Santiago=L[0]
  Valpo=L[1]
  SanAntonio=L[2]
  VillaAlemana=L[3]
  Melipilla=L[4]
  ConCon=L[5]
  Quilpue=L[6]
  Quillota=L[7]
  Quintero=L[8]
  Algarrobo=L[9]
  CasaBlanca=L[10]
  Curacavi=L[11]
  Puchuncavi=L[12]
  Maintencillo=L[13]
  Nogales=L[14]
  Catapilco=L[15]
  Calera=L[16]
  Llay=L[17]
  Felipe=L[18]
  Andes=L[19]
  Larga=L[20]
  Cumbre=L[21]
  Runge=L[22]
  Tabo=L[23]
  Vina=L[24]
  Flor=L[25]
  Monte=L[26]
  Lolenco=L[27]
  Cartagena=L[28]
  Leyda=L[29]
  Pange=L[30]
  Orozco=L[31]
  Placilla=L[32]
  Rosa=L[33]

  #################################################################################################################################################################################
  ############################################################################ VECINOS PRECONFIGURADO #############################################################################
  #################################################################################################################################################################################

  NRosa=list()
  NRosa.append(Curacavi)

  NOrozco=list()
  NOrozco.append(CasaBlanca)
  NOrozco.append(Placilla)

  NCartagena=list()
  NCartagena.append(SanAntonio)
  NCartagena.append(Tabo)
  NCartagena.append(Leyda)

  NAlgarrobo=list()
  NAlgarrobo.append(Tabo)

  NLolenco=list()
  NLolenco.append(Curacavi)
  NLolenco.append(Santiago)

  NSan=list()
  NSan.append(Larga)
  NSan.append(Runge)
  NSan.append(Flor)

  NMonte=list()
  NMonte.append(Flor)
  NMonte.append(Melipilla)

  NVal=list()  
  NVal.append(Vina)

  NConC=list() 
  NConC.append(Quilpue)
  NConC.append(Vina)
  NConC.append(Quillota) 

  NQuil=list() 
  NQuil.append(VillaAlemana)
  NQuil.append(Vina)
  NQuil.append(Orozco)

  NVilla=list()
  NVilla.append(Quillota)

  NQuintero=list()
  NQuintero.append(ConCon)
  NQuintero.append(Puchuncavi)

  NCasa=list()
  NCasa.append(Algarrobo)
  NCasa.append(Orozco)
  NCasa.append(Rosa)

  NPuchunca=list()
  NPuchunca.append(Maintencillo)
  NPuchunca.append(Nogales)

  NCatapilco=list()
  NCatapilco.append(Maintencillo)
  NCatapilco.append(Nogales)

  NCalera=list()
  NCalera.append(Nogales)
  NCalera.append(Llay)
  NCalera.append(Quillota)

  NVina=list()
  NVina.append(Quilpue)
  NVina.append(ConCon)
  NVina.append(Placilla)

  NPange=list()
  NPange.append(Melipilla)
  NPange.append(Leyda)

  NLlay=list()
  NLlay.append(Cumbre)
  NLlay.append(Felipe)

  NCumbre=list()
  NCumbre.append(Runge)

  NAndes=list()
  NAndes.append(Larga)
  NAndes.append(Felipe)

  NPlacilla=list()
  NPlacilla.append(Valpo)
  NPlacilla.append(Vina)

  #################################################################################################################################################################################
  ############################################################################ Creacion Camino ####################################################################################
  #################################################################################################################################################################################

  Edges(Map,VillaAlemana,NVilla)  
  Edges(Map,Santiago,NSan)  # Crea relaciones con peso entre NodoA y una lista de Nodos cercanos (neighbourhood), Santiago #Conce#Rancagua
  Edges(Map,Valpo,NVal)
  Edges(Map,Algarrobo,NAlgarrobo)
  Edges(Map,ConCon,NConC)
  Edges(Map,Quilpue,NQuil)
  Edges(Map,Quintero,NQuintero)
  Edges(Map,CasaBlanca,NCasa)
  Edges(Map,Puchuncavi,NPuchunca)
  Edges(Map,Catapilco,NCatapilco)
  Edges(Map,Calera,NCalera)
  Edges(Map,Cartagena,NCartagena)
  Edges(Map,Vina,NVina)
  Edges(Map,Llay,NLlay)
  Edges(Map,Andes,NAndes)
  Edges(Map,Cumbre,NCumbre)
  Edges(Map,Monte,NMonte)
  Edges(Map,Lolenco,NLolenco)
  Edges(Map,Pange,NPange)
  Edges(Map,Placilla,NPlacilla)
  Edges(Map,Orozco,NOrozco)
  Edges(Map,Rosa,NRosa)


  return None


#################################################################################################################################################################################
################################################################ Funciones Input Usuario ########################################################################################
#################################################################################################################################################################################


def ListCitysUser (): #Ciudades en el mapa definidas por el usuario
  
  L=list()
  x=0

  while True:
    Name=input("Ingrese nombre ciudad: ")
    posX=int(input("Ingrese Coordenadas X: ")) 
    posY=int(input("Ingrese Coordenadas Y: "))
    L.append(City(Name,posX,posY))
    Bool=int(input("Ingrese 1 para no continuar: "))
    NewNode(Map,L[x])
    x+=1

    if Bool==1:
      break

    print("\n")  

  return L

def ListEdgeUser(L,nameC):#Usuario va agregando conexiones entre ciudades
  
  G=list()
  
  for x in range(len(L)):

    Cit=input("Ingrese ciudad adyacente a "+nameC+": ")

    if L[x].name==Cit:
      G.append(L[x])
    
    Bool=input("Ingrese 1 para no continuar: ")

    if Bool==1:

      break

    print("\n") 

  return G


#################################################################################################################################################################################
###################################################################### MAIN #####################################################################################################
#################################################################################################################################################################################


G=list()
E=list()
Map= nx.Graph() #crea el mapa de la ciudad
L=ListCity(Map) #Inserta los nodos en la posx,y del mapa (sin conexiones) y retorna una lista con todos los nodos
ListEdges(L) #Crea las conexiones entre nodos
Current=L[2] #San Antonio
End=L[3] #Villa Alemana 3 , QUILLOTA 7
DistEu= Distance(Current,End) #Distancia directa entre los 2 nodos ignorando el camino (se utiliza para bsg en calculos posteriores)

#Path=Path_greed(Map,Current,End,G,E) #Lista con las ciudeades recorridas por el algoritmo greed dado un nodo inicial y un final, reemplazar este algoritmo con BFS u otros (?
Path=SearchAst(Map,Current,End,G,E)#Lista de ciudades recorridas por la heuristica Search A*

print (G[0],DistEu) #Distancia total recorrido y Distancia entre las 2 ciudades ignorando las conexiones
for x in range(len(Path)): #Imprime el nombre de las ciudades por la que paso
  print(Path[x].name)

pos = nx.get_node_attributes(Map,'pos') #parametro que se usa para dibujar en el mapa
Draw(Map,pos,Path,E) #Dibuja en el grafico las ciudades en rojo, y los caminos en verde es por donde paso el algoritmo
nx.draw_networkx_labels(Map, pos, NodesName(L) , font_color='black',font_size=11,font_family='Open Sans',font_weight='bold',alpha=0.7) #Dibuja en el grafico el nombre de las ciudades
plt.show() #Muestra el grafico