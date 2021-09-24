n=int(input('Dati numarul de elemente din vector='))
print('Introduceți ',n,' elemente pentru vectorul creat')
if n>9:
    print("Ați introdus un numar prea mare de elemente (maxim 9)")
    exit()
v=[]
for i in range(n):
    x=int(input('Introduceti elementul='))
    v.extend([x])

print('a)  afişează pe ecran componentele tabloului la un interval de 5 poziţii ', v[0:5])
v.reverse()
print('b)  afişează pe ecran numerele în ordinea inversă a introducerii în calculator ', v)
v.reverse()
b=sorted(v, reverse=True)
print('c)  sortează componentele tabloului în ordine descrescătoare ', b)
pare=[]
for i in v:
    if i%2==0:
        pare.append(i)
print('d)  afişează pe ecran doar componentele pare ', pare)
print('e)  afişează pe ecran media aritmetică a componentelor pare', sum(pare)/len(pare))
impare=[]
for i in v:
    if i%2!=0:
        impare.append(i)
print('f)  afişează pe ecran doar componentele impare', impare)
x=int(input('Introduceti valoarea lui x= '))
y=int(input('Introduceti valoarea lui y= '))
xy=[]
for i in v:
    if (i>x) and (i%y!=0):
        xy.append(i)
print('g)  afişează pe ecran doar componentele care sunt mai mari ca x şi nu sunt divizibile cu y (valorile x şi y se citesc de la tastatură) ', xy)
x=int(input('Introduceti valoarea lui x= '))
y=int(input('Introduceti valoarea lui y= '))
xy2=[]
for i in v:
    if (i>x) and (i<y):
        xy2.append(i)
print('h)  afişează pe ecran doar componentele care sunt mai mari ca x şi mai mici decât y (valorile x şi y se citesc de la tastatură) ', xy2)
c=-1
poz=[]
for i in v:
    c+=1
    if (i<0) and (i%2!=0):
        poz.append(c)
print('i)  afişează pe ecran poziţiile (indicii) componentelor impare negative', poz)
c=-1
cif2=[]
for i in v:
    c+=1
    if (i>9 and i<100) or (i<-9 and i>-100):
        cif2.append(c)
print('j)  afişează pe ecran poziţiile (indicii) componentelor ce conţin doar două cifre semnificative', cif2)
v2=list(v)
v2[0]=min(v)
print('k)  înlocuieşte prima componentă a tabloului cu componenta de valoare minimă din tabloul respectiv', v2)
c=-1
v2=list(v)
for i in v:
    c+=1
    if i==min(v):
        v2.pop(c)
        v2.insert(c, v2[0])
print('l)  înlocuieşte componenta de valoare minimă din tabloul respectiv cu prima componentă a acestuia', v2)
pare=[]
for i in v:
    if i%2==0:
        pare.append(i)
print('m)  creează un tablou nou, format doar din componentele pare ale tabloului introdus de la tastatură', pare)
div3=[]
for i in v:
    if i%3 == 0:
        div3.append(i)
print('n)  creează un tablou nou, format doar din componentele divizibile cu 3 ale tabloului introdus de la tastatură', div3)
div4=[]
c=0
for i in v:
    for diviz in range(1,i+1):
        if i%diviz==0:
            c+=1
    if c<=4:
        div4.append(i)
print('o)  creează un tablou nou, format doar din acele componente ale tabloului introdus de la tastatură care au cel mult patru divizori', div4)