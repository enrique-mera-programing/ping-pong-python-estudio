
hola=int(input('digite algo')) 
print(hola + 1)
array=["hola",'mundo','sebas']
concatenacion=""
for i,hola in enumerate(array):
    espacio=""
    if i!=0:
        espacio=" "
    print(i)
    concatenacion+=espacio+hola
i=1
total=0
while i>0:
    
    numero=int(input('dame un numero: '))
    if numero==0:
        break
    total+=numero
    i+=1
print("total= " + str(total) )
