import persona
dato = int(input("ingrese un valor: "))

print(dato)

if (dato > 0):
    print("Es positivo")
else:
    if (dato < 0):
        print("Es negativo")
    else:
        print("Es cero")

"while"
x = 1
while (x < dato):
    print(x)
    x = x + 1
    
"for"

for x  in range (0,100, 2):
    print(x)

palabra = "Palabra"
for letra in palabra:
    print(letra)

def saludo(nombre):
        print("hola como estas ",dato)

saludo(dato)

tupla = ('A','B','C','D')

print(tupla)

yo = persona.Persona('osskr', 29, 'Argentino')

yo.saludar() 

archivo = open('file.txt','a')
archivo.write('escribo una linea en el archivo')
archivo.close()