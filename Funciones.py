from random import shuffle
import random
import math

# Probabilidad
def Probabilidad():
    ra=round(random.random(),2)
    return ra
#Poblacion
def cadenaN(numerolimite):
    x = [i for i in range(1,numerolimite)]
    shuffle(x)
    return x
#Valoracion
def valoracion(Matriz,np):
    Valor = []
    contador = 0
    for m in range(np):
        matriz=Matriz[m]
        for i in range(8):
            oi = matriz[i]
            for j in range(8):
                oj=matriz[j]
                if(i != j):
                    _v1=math.fabs(oi-oj)
                    _v2=math.fabs(i-j)
                    if(_v1 == _v2):
                        contador=contador+1
        contador=round(contador/2,0)
        Valor.append(contador)
        contador=contador*0
    return Valor
# torneo
def torneo(valores, poblacion):
    Ganadores = []
    for i in range(2):
        a1 = random.randrange(1,poblacion)
        a2 = random.randrange(1,poblacion)
        bandera=True
        while(bandera):
            if(a1 == a2 ):
                    a2=random.randrange(1,poblacion)
                    a1=random.randrange(1,poblacion)
            else:
                bandera=False
        aa1 = valores[a1]
        aa2 = valores[a2]
        if (aa1  < aa2):
            Ganadores.append(a1)
        else:
            Ganadores.append(a2)
    return Ganadores
#cruse
def cruse(Ganadores,matriz):
    hijos = []
    hijo = []
    Ganadores[0]=Ganadores[0]-1
    Ganadores[1]=Ganadores[1]-1
    a1 = random.randrange(1,8)
    #print('Alelo donde se segmenta: ',a1)
    ax1=a1
    for j in range(2):
        for i in range(a1):
            hijo.append((matriz[Ganadores[j]][i]))
        for m in range (8):
            if(j==0):
                a=hijo.count(matriz[Ganadores[1]][m])
                if(a==0):
                    hijo.insert(ax1, matriz[Ganadores[1]][m])
                ax1=ax1+1
            else:
                a = hijo.count(matriz[Ganadores[0]][m])
                if(a==0):
                    hijo.insert(ax1, matriz[Ganadores[0]][m])
                ax1=ax1+1
        hijos.append(hijo)
        hijo=hijo*0
        ax1=a1
    return hijos
#mutacion
def mutacion_un_hijo(hijo):
    r1 = random.randrange(8)
    r2 = random.randrange(8)
    G1 = hijo[r1]
    G2 = hijo[r2]
    hijo[r1] = G2
    hijo[r2] = G1
    return hijo
#seleccion
def seleccion(padres,hijos,matriz):
    padres[0]=padres[0]-1
    padres[1]=padres[1]-1
    if(hijos[0]<matriz[padres[0]]):
        ax="[11]"
    else:
        ax="[0]"
        #print("sin Cambios entre el hijo 1")
    if(hijos[1]<matriz[padres[1]]):
        ax=ax+" [22]"
    else:
        ax="[0]"
        #print("sin Cambios entre el hijo 2")
    return ax