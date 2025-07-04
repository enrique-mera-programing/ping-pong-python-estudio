
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

print(concatenacion)
