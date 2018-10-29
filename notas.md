# Notas para python

Este repositorio contiene las notas para lo que vaya aprendiendo de python, no es algo formal sino mas bien una forma de recordar rapido algunos conceptos.

## Obtener datos por consola

para obtener datos por consola en python utilizamos la funcion  `input()` de la siguiente manera:

```python
dato = input("ingrese un dato:")
```

esto nos captura un dato de cualquier tipo, podemos especificar el tipo de dato que esperamos, de la siguiente manera:

```python
dato = int(input("ingrese un dato numerico:"))
```

## Condicionales

### if

El if tiene la siguiente estructura

```python

if(condicion):
    //statements
else:
    //statements
```

En este ejemplo vemos un if anidado

```python
dato = 9

if (dato > 0):
    print("Es positivo")
else:
    if (dato < 0):
        print("Es negativo")
    else:
        print("Es cero")
```

## Ciclos

### While

```python
x = 1
while (x < 10):
    print(x)
```

### For

La estructura basica del ciclo for es la siguiente:

```python
for x in range (1,10):
    print(x)
```

tambien podemos usar un parametro adicional en `range()` para especificar los pasos en la iteracion, en este caso la iteracion seria de 2 en 2.

```python
for x in range (1,10,2):
    print(x)
```

esta seria una forma para recorrer un string e imprimir caracter por caracter

```python
palabra = "Palabra"

for letra in palabra:
    print(letra)
```

## Funciones

Para definir funciones usamos la palabra reservada `def` y definimos la funcion de la siguiente manera

```python
def miFuncion(parametros):
    "codigo"
    return algo
```

por ejemplo

```python
def saludo(nombre):
    print("hola como estas ", nombre)
```

para llamar la funcion que acabamos de crear utilizamos

`saludo(nombre)`

## Estructuras de datos

### Listas

Una lista es un valor que contiene multiples valores en una secuencia ordenada en python una lista se ve de la siguiente manera `['tomate','lechuga','oregano','carne']`, cada uno de los elementos de la lista van separados por comas `,` y los llamamos items.

Una lista de strings :

`['juan','carlos','maria','susana']`

Una lista de enteros :

`[1,2,3,4,6,76,4]`

podemos asignar una lista a una variable

`mascotas = ['perro','gato,'conejo','hamster']`

para acceder a los elementos de la lista de manera individual lo hacemos mediante sus indices, empezando desde 0

```python
mascotas[0]
>>> 'perro'
mascotas[1]
>>> 'gato'
mascotas[2]
>>> 'conejo'
mascotas[3]
>>> 'hamster'
```

#### listas con indices negativos

una caracteristica interesante es que podemos usar indices(enteros) negativos, el valor -1 se va referir al ultimo elemento de la lista , -2 al anteultimo y asi sucesivamente.

```python
mascotas[-1]
>>> 'hamster'
mascotas[-2]
>>> 'conejo'
mascotas[-3]
>>> 'gato'
mascotas[-4]
>>> 'perro'
```

#### Listas de listas

las listas tambien pueden contener como items a otras listas

`multiLista = [[1,2,3,4],['perro','gato,'conejo','hamster']`

para acceder a los items de estas listas usamos primero el indice de la lista donde se encuentra el item al que queremos acceder y luego el indice del item al que queremos acceder dentro de esa lista

```python
multiLista[1][1]
>>> 'gato'
multiLista[0][3]
>>> 4
```

#### Obteniendo sublistas con Slices

Podemos obtener partes de una lista para formar nuevas listas

`nombres =['juan','carlos','maria','susana']`

para obtener un solo elemento usamos

```python
unNombre = nombres[2]
>>> 'maria'
```

para obtener varios elementos en una nueva lista

```python
subListaDeNombres = nombres[1:3]
>>> '['carlos','maria']'
```

el primer indice del slice nos dice el item de la lista donde comienza  y el segundo item donde finaliza este ultimo no se incluye en la nueva lista.

#### Cantidad de elementos de una lista

Para obtener la cantidad de elementos en una lista utilizamos la funcion `len()` :

```python
len(nombres)
>>> 4
```

#### Cambiar valores a los items de una lista

Podemos alterar el valor de un item de la lista de la siguiente manera

```python
nombres =['juan','carlos','maria','susana']
nombres[1] = 'rodolfo'
>>>> ['juan','rodolfo','maria','susana']
```

#### Concatenar y replicar listas

El operador `+` puede combinar 2 listas para formar una nueva, de la misma manera que hace con los strings.

```python
[1,2,3] + ['A','B','C']
>>> [1,2,3,'A','B','C']
```

 El operador `*` se puede usar con una lista y un entero para  para replicar la lista

```python
['Q','W','E']*3
>>> ['Q','W','E','Q','W','E','Q','W','E']
```

#### Eliminando elementos de una lista

Con la palabra reservada `del` [^1] podemos eliminar items de una lista

```python
nombres =['juan','carlos','maria','susana']
del nombres[1]
>>>> ['juan','maria','susana']
```

[^1]: `del` tambien sirve para eliminar variables simples como si se tratara de un "desasignador" de variables pero en la practica no es muy utilizado.

### Tuplas

Las tuplas son muy similares a las listas a excepcion de dos cosas
la primera es que utilizamos parentesis `(and)` para declararlas en cambio de los corchetes `[]` usados en las listas

`('perro','gato','conejo')`

y la segunda diferencia (y la mas importante) que estas tienen con las listas es que las tuplas son inmutables. Esto quiere decir que no se puede  agregar, eliminar o modificar elementos de una tupla luego de que esta fue declarada.

```python
tupla = ('A','B','C','D')
tupla[1] = 'z'

>>>Traceback (most recent call last):
  File "pruebas.py", line 34, in <module>
    tupla[1] = 'z'
TypeError: 'tuple' object does not support item assignment
```

Si queremos tener un solo item en nuestra tupla, debemos indicar esto poniendo una coma  despues del item, de lo contrario python va a interpretar que estamos declarando un valor simple dentro de un partentesis

`tuplaDeUnSoloItem = ('item',)`

### Convirtiendo tuplas a listas con list( ) y tuple( )

las funciones `list()` y `tuple()` retornan una lista o una tupla respectivamente de los valores que se pasen como argumentos

```python
tuple(['casa','departamento','quinta'])
>>>('casa','departamento','quinta')
devuelve una tupla

list(['casa','departamento','quinta'])
>>>['casa','departamento','quinta']
devuelve una lista
```

Las tuplas dan una pista a quien este leyendo nuestro codigo de que los datos que representamos no estan pensados para ser cambiados luego de su declaracion.

### Diccionarios

Asi como las listas los diccionarios son una coleccion de valores, pero a diferencia de las listas en las cualeslos indices son enteros, los diccionarios pueden tener distintos tipos de datos como indices.

Los indices para los diccionarios se llaman, llaves (*keys*) y las llaves se encuentran asociadas a valores (*values*) y en conjuncion los llamamos pares clave-valor (*key-value*)

para declarar un diccionario utilizamos llaves `{}`, veamos un ejemplo

```python
miDic = {'size':'fat', 'color':'gray','age':'20'}
```

en este caso tenemos las llaves `'size', 'color', 'age'` y los correspondientes valores `'fat', 'gray', '20'`

podemos acceder a los valores a traves de sus correspondientes claves

```python
miDic['color']
>>> 'gray'
```

los diccionarios pueden usar claves integer al igual que las listas pero estas no necesariamente deben empezar desde 0 pueden ser cualquier numero

```python
miDic = {122:'key 1', 12653:'new value', 34:'you got it'}
```

#### Diccionarios vs Listas

A diferencia de las listas los diccionarios no tienen un orden, esto es logico porque sus claves no tienen que cumplir con ningun orden. mientras el orden tiene importancia a la hora de determinar si dos listas son la misma, en el caso de los diccionarios no importa el orden de los pares llave-valor estan tipeados.

```python
l1 = ['casa','departamento','quinta']
l2 = ['departamento','casa','quinta']
l1 == l2
>>> False

eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
eggs == ham
>>>True
```

debido a que los diccionarios no tienen ningun orden en particular, no podemos obtener "sub diccionarios" como en el caso de las listas.

#### Los metodos .keys() .values() .items()

Los valores retornados por estos metodos pueden ser utilizados en loops *for*

* *values( )*

Retorna algo similar a una lista con los valores del diccionario

```python
spam = {'color': 'red', 'age': 42}
for v in spam.values():
    print(v)

>>> red
>>>42
```

* *keys( )*

Retorna algo similar a una lista con las claves del diccionario

```python
spam = {'color': 'red', 'age': 42}
for k in spam.keys():
    print(k)

>>> color
>>> age
```

* *items( )*

Retorna algo similar a una lista con los pares clave-valor del diccionario

```python
for i in spam.items():
    print(i)

>>>('color', 'red')
>>>('age', 42)
```

*Nota: si queremos que los valores retornados por los metododos items( ), keys( ) y values( ) sean listas podemos usar el metodo list() visto anteriormente.*

tambien podemos usar una asignacion multiple en un *for( )* para asignar asignar la clave y el valor a variables separadas

```python
spam = {'color': 'red', 'age': 42}
for k, v in spam.items():
    print('Llave: ' + k + ' Valor: ' + str(v))

>>> Llave: age Valor: 42
>>> Llave: color Valor: red
```

#### Chequeando si un valor o una clave extisten en un diccionario

Asi como en las listas los operadores *in* y *not in* pueden chequear si cierto valor o clave existen en un diccionario

```python
spam = {'name': 'Zophie', 'age': 7}

'name' in spam.keys()
>>> True

'Zophie' in spam.values()
>>> True

'color' in spam.keys()
>>> False

'color' not in spam.keys()
>>> True

'color' in spam
>>> False
```

#### El metodo *get( )*

El metodo *get( )* toma 2 argumentos  la clave del valor a devolver y un valor por defecto ( *fallback value* ) en caso de que esa clave no exista. Este metodo nos evita tener que hacer una comprobacion con *in*  para saber la clave existe en el diccionario.

```python
picnicItems = {'apples': 5, 'cups': 2}
'I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.'

>>> 'I am bringing 2 cups.'

'I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.'

>>> 'I am bringing 0 eggs.'
```

#### el metodo *setDefault( )*

A menudo necesitaremos ingresar un valor en un diccionario para cierta clave, solo si esa clave actualmente no tiene un valor. Esto nos significaria comprobar si la clave existe y luego agregar el valor, lo cual se puede volver un poco tedioso en ciertos casos. El metodo *setDefault( )* nos permite hacer esto en una sola linea de codigo

```python
spam = {'name': 'Pooka', 'age': 5}
spam.setdefault('color', 'black')
>>>'black'

spam
{'color': 'black', 'age': 5, 'name': 'Pooka'}
spam.setdefault('color', 'white')
>>>'black'

spam
>>>{'color': 'black', 'age': 5, 'name': 'Pooka'}
```

## Programacion Orientada a Objetos

### Clases

Para definir una clase en python utilizamos la palabra reservada *class( )*

```python
class Persona:
    nombre =""
    edad = 0
    nacionalidad = ""

    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad


    def saludar(self):
        print("hola mi nombre es ", self.nombre)
 ```

Con  _init( )_  definimos el construcctor de una clase

## Archivos

Hay tres pasos a seguir para el trabajo con archivos en python

1. llamar a la funcion *open()* para que nos devuelva un objeto del tipo *File*

2. llamar al metodo *read()* or *write()* en el objeto *File* creado

3. Cerrar el archivo invocando al metodo *close( )* del objeto *File*

tenemos 3 modos para abrir los archivos:

* *'r'* : abre el archivo en modo de solo lectura.
* *'w'* : abre el archivo en modo escritura, si no existe lo crea en la ruta especificada en open y si existe lo sobreescribe.
* *'a'* : abre el archivo en modo de escritura pero si este existe no lo sobreescribe.

### Abrir un Archivo

para abrir un archivo hacemos lo siguiente:

```python
miArchivo = open('ruta del archivo','r')
```

con el parametro *'r'*  de la funcion open estamos indicando el modo en el que queremos abrir el archivo

### Crear un Archivo y sobreescribir su contenido

para abrir un archivo hacemos lo siguiente:

```python
miArchivo = open('ruta del archivo','w')
```

### Abrir archivo existente en modo de escritura sin sobreescribir

para abrir un archivo existente al cual le queremos seguir agregando lineas sin que sea sobreescrito hacemos lo siguiente:

```python
miArchivo = open('ruta del archivo','a')
```

### Cerrar archivos

Siempre que abrimos un archivo y luego de que terminemos de trabajar con el debemos cerrarlo, para esto llamamos al metodo *close()*

```python
miArchivo.close()
```

### Escribir en un archivo

Para escribir en un archivo primero abrimos el archivo en modo *'a' (append)* y luego llamamos al metodo *write( )* para agregar lineas al final del archivo

```python
miArchivo = open('mi archivo en disco.txt'.'a')
miArchivo.write('Agregamos una linea al archivo')
miArchivo.close()
```