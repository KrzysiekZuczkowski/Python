import matplotlib.pyplot as plt
import numpy as np


def maksymalny(A):
    m = A[0]
    for i in range(1, len(A)):
        if A[i] > m:
            m = A[i]
    return m

def minimalny(A):
    m = A[0]
    for i in range(1, len(A)):
        if A[i] < m:
            m = A[i]
    return m

def zamien(n):
    p = n[0]
    n[0] = n[1]
    n[1] = p
    return n

ax1 = [5, 5]
ay1 = [3.2, 8.4]

ax2 = [1, 5]
ay2 = [9, 4]

if ax1[0] > ax1[1]:
    zamien(ax1)
    zamien(ay1)
    
if ax2[0] > ax2[1]:
    zamien(ax2)
    zamien(ay2)
    
kp = minimalny(ax1 + ax2)
kk = maksymalny(ax1 + ax2)

X1 = range(minimalny(ax1), maksymalny(ax1) + 1)
X2 = range(minimalny(ax2), maksymalny(ax2) + 1)

A = [ 0 for i in range(kk + 1) ]

for i in (X1 + X2):
    A[i] = A[i] + 1


B = []
for i in range(kp, kk + 1):
    if A[i] > 1:
        B.append(i)


wynik = False

if ax1[0] == ax1[1]:
    sn = 0
else:
    sn = float((ay1[1] - ay1[0])) / (ax1[1] - ax1[0])

if ax2[0] == ax2[1]:
    sc = 0
else:
    sc = float((ay2[1] - ay2[0])) / (ax2[1] - ax2[0])

if B:
    Cx1 = [ 0 for i in range(X1[-1] + 1) ]
    Cx2 = [ 0 for i in range(X2[-1] + 1) ]
    Cx1[X1[0]] = ay1[0]
    Cx2[X2[0]] = ay2[0]
    for i in range(1, len(X1)):
        Cx1[X1[i]] =  Cx1[X1[i - 1]]  + sn 

    for i in range(1, len(X2)):
        Cx2[X2[i]] =  Cx2[X2[i - 1]]  + sc

    if ax1[0] == ax1[1]:
        if ax2[0] == ax2[1]:
            if minimalny(ay2) in range(maksymalny(ay1)):
                y = minimalny(ay2)
            elif maksymalny(ay2) in range(maksymalny(ay1)):
                y = maksymalny(ay2)
            wynik = True
            x = B[0]
        elif ( np.round(Cx2[B[0]], 6) <= ay1[0] and np.round(Cx2[B[0]], 6) >= ay1[1] ) or ( np.round(Cx2[B[0]], 6) >= ay1[0] and np.round(Cx2[B[0]], 6) <= ay1[1] ):
            wynik = True
            x = B[0]
            y = Cx2[x]
    elif ax2[0] == ax2[1]:
        if ( np.round(Cx1[B[0]], 6) <= ay2[0] and np.round(Cx1[B[0]], 6) >= ay2[1] ) or ( np.round(Cx1[B[0]], 6) >= ay2[0] and np.round(Cx1[B[0]], 6) <= ay2[1] ):
            wynik = True
            x = B[0]
            y = Cx1[x]
    elif ( np.round(Cx1[B[0]], 6 ) >= np.round(Cx2[B[0]], 6) and np.round(Cx1[B[-1]], 6) <= np.round(Cx2[B[-1]], 6) ) or ( np.round(Cx1[B[0]], 6) <= np.round(Cx2[B[0]], 6) and np.round(Cx1[B[-1]], 6) >= np.round(Cx2[B[-1]], 6) ):
        wynik = True
        i = X1[0]
        m = minimalny(Cx1[i:])
        while Cx1[i] != m:
            i += 1

        j = X2[0]
        m = minimalny(Cx2[j:])
        while Cx2[j] != m:
            j += 1

        lewy = B[0]
        prawy = B[-1]
        srodek = float( lewy + prawy ) / 2
        kn = minimalny(ay1) + sn * ( srodek - i )
        kc = minimalny(ay2) + sc * ( srodek - j )
        if sn > 0:
            while lewy < prawy and kn != kc:
                if kn > kc:
                    prawy = srodek - 0.00000001
                else:
                    lewy = srodek + 0.00000001
                srodek = float( lewy + prawy ) / 2
                kn = minimalny(ay1) + sn * ( srodek - i )
                kc = minimalny(ay2) + sc * ( srodek - j )
                
            x = np.round(srodek, 6)
            y = np.round(kn, 6)
        elif sn == 0:
            x = (kn - minimalny(ay2)) / sc
            x = j + x
            y = kn
        else:
            while lewy < prawy and kn != kc:
                if not kn > kc:
                    prawy = srodek - 0.00000001
                else:
                    lewy = srodek + 0.00000001 # lewy
                srodek = float( lewy + prawy ) / 2
                kn = minimalny(ay1) + sn * ( srodek - i )
                kc = minimalny(ay2) + sc * ( srodek - j )

            x = np.round(srodek, 6)
            y = np.round(kn, 6)
        
if wynik:
    print 'odcinki maja punkt wspolny (przecinaja sie) w x =', x, 'y =', y
else:
    print 'brak punktu wspolnego (przeciecia odcinkow)'

plt.plot( ax1 , ay1, color='blue',  linewidth=2, markersize=12)
plt.plot( ax2 , ay2 , color='red',  linewidth=2, markersize=12)
plt.axis([0, 10, 0, 10 ])
plt.xlabel('niebieski ' + str(sn) + '   czerwony ' + str(sc))
#plt.legend(['niebieski ' + str(sn) + '\nczerwony ' + str(sc)], loc='upper left')
plt.grid(True)
plt.show()
