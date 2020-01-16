# -*- coding: cp1250 -*-
from random import randint
import matplotlib.pyplot as plt
import numpy as np
import math


board = []      # tablica wspołrzędnych
x = []          # lista współrzędnych x
y = []          # lista współrzędnych y
xplt = []
yplt = []
minkoszt = 10000
#tabela pomocnicza 
for i in range(125):
    board.append(["*"] * 125) 

#losowanie wspolrzendnej y
def random_row(board):
    return randint(0, len(board) - 1)

#losowanie wspolrzednej x
def random_col(board):
    return randint(0, len(board[0]) - 1)

# generowanie losowo punktow (miasta)
def miasta(n):
    for turn in range(n):
        v_row = random_row(board)
        v_col = random_col(board)
        while board[v_row][v_col] == "X":
            v_row = random_row(board)
            v_col = random_col(board)
        board[v_row][v_col] = "X"
        x.append(v_row) 
        y.append(v_col)

# obliczanie dystansu pomiędzy dwoma wybranymi miastami
def dystans(x1, y1, x2, y2):
    dx, dy = x2 - x1, y2 - y1
    return math.sqrt((dx * dx) + (dy * dy))

# wyświetlanie miast i trasy pomiedzy nimi
def wyswietl(pkt):
    if (pkt == 1):
        plt.plot(x , y , 'bs')
        plt.title('Wszystkie miasta')
    else:
        print "wspolrzedne x trasy : ", xplt
        print "wspolrzedne y trasy : ", yplt
        plt.plot(xplt , yplt ,marker='8', color = 'b')
        plt.title('Najkrotsza droga przez wszystkie miasta')
    plt.axis([0, 125, 0, 125 ])
    plt.xlabel('Szerokosc')
    plt.ylabel('Wysokosc')
    plt.grid(True)
    plt.show()

#wyznaczenie tablicy wag
def wyznaczWagi(wagi, x, y):
    for i in range(n):
        wagi.append([0.] * n)
    for i in range(n):
        for j in range(n):
             wagi[i][j] = (dystans(x[i], y[i], x[j], y[j]))
    return wagi

#tworzy listy wspolrzednych
def wyznaczTrase(trasa, xplt, yplt):
    for i in trasa:
        xplt.append(x[i])
        yplt.append(y[i])

#wyznacza koszt przebiegu trasy
def wyznaczKoszt(trasa, koszt):  
    for i in range(len(trasa) - 1):
        koszt = koszt + wagi[trasa[i]][trasa[i+1]]
    return math.ceil(koszt)
        
'''
for turn in range(n/2):
    v_row = v_col = 0
    while [v_row] == [v_col]:
        v_row = random_row(wagi)
        v_col = random_col(wagi)
    wagi[v_row][v_col] = wagi[v_row][v_col] + (turn + 1)
'''

n = int(input("podaj liczbę miast "))
miasta(n)
wagi = []
wyznaczWagi(wagi, x, y)
'''
for row in wagi:
   print row
'''
koszt1 = 10000
for j in range(n):
    s1  = j  # wierzchlek 0 to x[0] i y[0] czli pierwszy z listy wspolrzednych x i y len(n_row) - 1 #randint(0, len(n_row) - 1)   # wybor zrodla s
    w1 = 0
    lista_wierzch = range(len(x))
    lista_wierzch.remove(s1)
    tablica_wag1 = range(n)
    while len(lista_wierzch) > 0:
        for i in range(n):
            tablica_wag1[i] = "X"
        for i in lista_wierzch: # numer indeksu jest zarazem wierzcholkiem
            tablica_wag1[i] = wagi[s1][i] + w1
        w1 = min(tablica_wag1)
        s1 = tablica_wag1.index(w1)
        lista_wierzch.remove(s1)
    koszt = math.floor(w1 + wagi[s1][j] - 50)
    if koszt < koszt1:
        koszt1 = koszt

'''
Koszt sam w sobie jest karą, dlatego warto go zmniejszyć.
Koszt1 wyraża wartość wstempną, celowo zaniżoną o 50 tak aby udana próba jej zrealizowania,
pozwalała na pokonanie trasy krótszą scieżką, co z kolei staje się nagrodą. 
'''

print "wspolrzedne x ", x
print "wspolrzedne y ", y

wyswietl(1)

print "Koszt zanizony o 50 : ", koszt1
ngr = n
for j in range(ngr):
    lista_wierzch = range(len(x))
    s1 = s2 = j
    w1 = w2 = 0
    lista_wierzch.remove(s1)
    trasa1 = []
    trasa2 = []
    trasa1.append(s1)
    trasa2.append(s2)
    tablica_wag1 = range(n)
    tablica_wag2 = range(n)
    while len(lista_wierzch) > 0:
        for i in range(n):
            tablica_wag1[i] = "X"
            tablica_wag2[i] = "X"
        for i in lista_wierzch: 
            tablica_wag1[i] = wagi[s1][i] + w1
            tablica_wag2[i] = wagi[s2][i] + w2
        if min(tablica_wag1) <= min(tablica_wag2):
            w1 = min(tablica_wag1)
            s1 = tablica_wag1.index(w1)
            trasa1.append( s1 )
            lista_wierzch.remove(s1)
        else:
            w2 = min(tablica_wag2)
            s2 = tablica_wag2.index(w2)
            trasa2.append( s2 ) 
            lista_wierzch.remove(s2)
    trasa2.reverse()
    for i in trasa2:
        trasa1.append(i)
    koszt = 0
    koszt = wyznaczKoszt(trasa1, koszt)
    if koszt <= koszt1:
        print "Koszt osiagniety * : ", koszt
        wyznaczTrase(trasa1, xplt, yplt)
        wyswietl(2)
        break
    elif koszt < minkoszt:
        minkoszt = koszt
        trasa = list(trasa1)
    if j == ngr - 1:
        for i in range(1, n - 1):
            trasa2 = list(trasa)
            trasa2[i], trasa2[i + 1] = trasa2[i + 1], trasa2[i] 
            koszt = 0
            koszt =  wyznaczKoszt(trasa2, koszt)
            if koszt < minkoszt:
                minkoszt = koszt
                trasa = list(trasa2)
        xplt = []
        yplt = []
        wyznaczTrase(trasa, xplt, yplt)
        print "Koszt osiagniety : ", minkoszt
        wyswietl(2)
