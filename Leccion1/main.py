'''
miVariable = 3
print(miVariable)
miVariable = 'Hola a todos los estudiantes de la tecnicatura'
print(miVariable)
miVariable = 3.5
print(miVariable)

x = 10
y = 2
z = x + y

print(id(x))
# Las literales se escriben x176 (esto es el espacio en la memoria de una variable, cuandoi ejecutemos de nuevo
# cambia el numero, solo tomamos los ultimnos 3

print(id(y))
print(id(z))

# tipos int, Float, String, Bool
x = 10
print(x)
print(type(x))
x = 14.5
print(x)
print(type(x))
x = 'Hola alumnos'
print(x)
print(type(x))
x = True
print(x)
print(type(x))
x = False
print(x)
print(type(x))

# manejo de cadenas (String)
miGrupoFavorito = 'Bon Jovi' + ' ' + 'los más piola'
caracteristicas = 'Los más copados'
print('Mi grupo favorito es: ' + miGrupoFavorito + ' ' + caracteristicas)
# print('Mi grupo favorito es: ', miGrupoFavorito, caracteristicas)

numero1 = '7'
numero2 = '8'
print(int(numero1) + int(numero2))

# tipos Boleanos (bool)
miBooleano = 3 > 2
print(miBooleano)

if miBooleano:
    print('El resultado es verdadero')
else:
    print('El resultado es falso')

# Procesar la entrada del usuario
# funcion input
# resultado = input('Digite un numero: '  # input regresa un dato tipo string
# print(resultado)

# conversion de la entrada de datos
numero1 = int(input('Escribe el primer numero: '))
numero2 = int(input('Escribe el segundo numero: '))
resultado = numero1 + numero2
print('El resultado de la suma es: ', resultado)


# tarea1

resul = input('como estuvo tu día?  Entre 1 y 10 : ')
print('Mi día estuvo: ' + resul + ' puntos')

# tarea 2
titulo = input('proporcione el titulo del libro: ')
autor = input('proporciona el autor del libro: ')
print(titulo, 'fue escrito por:', autor)

#-----------Operadores aritmeticos-------------

operandoA = 8
operandoB = 5
suma = operandoA + operandoB
#print ('Resultado de la suma es: ', suma)
print (f'Resultado de la suma es: {suma}')


resta = operandoA - operandoB
print(f'El resultado de la resta es: {resta}')

multiplicacion = operandoA * operandoB
print(f'El resultado de la multiplicación es: {multiplicacion}')

division = operandoA / operandoB
print(f'El resultado de la división es: {division}')

#acá es para que lo haga entero
division = operandoA // operandoB
print(f'El resultado de la división (int) es: {division}')

modulo = operandoA % operandoB   #porq es 8/3 y el residuo es lo q sobra
print(f'El resultado de la disión o residuo es: {modulo}')

exponente = operandoA ** operandoB (8 a la 5)
print(f'El resultado del exponente es: {exponente}')
'''

# ----------área y perímetro de un rectángulo----------
# input es tipo string o espera un string por eso le ponemos el int (q es entero) para q lo tome como numero
'''
alto = int(input('Escribe el alto del rectángulo: '))
ancho = int(input('Escribe el ancho del rectángulo: '))


area = alto * ancho
print(f'El área del rectángulo es: {area}')

perimetro = (alto + ancho) * 2
print(f'El perímetro del rectángulo es: {perimetro}')
'''

'''
#-- asiganacion & comparacion
miVariable3 = 10
print(miVariable3)

#operadores de reasignación
miVariable3 = miVariable3 + 1
print(miVariable3)

miVariable3 += 1
print(miVariable3)

# miVariable3 = miVariable3 -2
miVariable3 -= 2
print(miVariable3)

# miVariable3 = miVariable3 *3
miVariable3 *= 3
print(miVariable3)

# miVariable3 = miVariable3 /2
miVariable3 /= 2
print(miVariable3)

#--  comparacion

d = 4
b = 2
resultado = d == b #comprobamos si son iguales
print(resultado)

# operador diferente
resultado = d != b
print(resultado)

# operador Mayor que
resultado = d > b
print(resultado)

# operador Menor que
resultado = d < b
print(resultado)

# operador Menor o igual que
resultado = d <= b
print(resultado)

# operador Mayor o igual que
resultado = d >= b
print(resultado)

# par o impar

a = int(input('Escribe un número: '))
print(f'El residuo de la división es: {a % 2}')
if a % 2 == 0:
    print(f'{a} Es un número par')
else:
    print(f'{a} Es un número impar' )


#si es mayor de edad

a = int(input('Escribe la edad: '))
# print(f'El residuo de la división es: {a % 2}')
if a >= 18:
    print(f'{a} Es mayor de edad')
else:
    print(f'{a} Es menor de edad' )

#otra manera es:
edadAdulta = 18
edadPersona = int(input('Digite su edad: '))
if edadPersona >= edadAdulta:
    print(f'Su edad es: {edadPersona} años, es mayor de edad')
else:
    print(f'Su edad es: {edadPersona} años, es menor de edad')
'''
'''
# Operadores Lógicos
a = True
b = True
resultado = a and b
print(resultado)

# operador or
resultado = a or b
print(resultado)

# operador not
resultado = not a
print(resultado)

# Valor de un rango

valor = int(input('Escribe un numero del 0 a 5: '))
valorMaximo = 5
valorMinimo = 0

dentroRango = (valor >= valorMinimo and valor <= valorMaximo)
if dentroRango:
    print(f'El valor {valor} esta dentro del rango')
else:
    print(f'El valor{valor} No esta dentro del rango')
'''
'''
    #Operador or

vacaciones = False
diaDescanso = False
if vacaciones or diaDescanso:
    print('Puede asistir al juego')
else:
    print('Tiene trabajo que hacer')

    vacaciones = False
    diaDescanso = False
    if not(vacaciones or diaDescanso):
        print('Puede asistir al juego')
    else:
        print('Tiene trabajo que hacer')

'''

'''
#operador and 20 y 30 años  or

edad = int(input('Escriba su edad: '))
veinte = edad >= 20 and edad < 30
print(veinte)
treinta =  edad >= 30 and edad < 40
print(treinta)

if veinte or treinta:
    #if(edad >= 20 and edad < 30) or (edad >= 30 and < 40):
    #print("Estas dentro del rango de los (20'0) a (30'0) años")
    #esta es la forma en la q habitualmente se hace

    #sintaxis simplificada del operador and
    #if veinte or treinta:
    #if (20 <= edad < 30) or (30 <= edad <40):


    print('Estas dentro del rango de los (20\'0) a (30\'0) años')

else:
    print("No estas dentro del rango de los (20\'0) a (30\'0) años")
    #funciona \para distinguir con la ' pero si usamos " no hace falta poner \

'''
if veinte:
    print('Estas dentro del rango de los (20\'0) a (30\'0) años')

elif treinta:
    print('Estas dentro del rango de los (30\'0) años')

else:
    print("No estas dentro del rango de los (20\'0) a (30\'0) años")
    #funciona \para distinguir con la ' pero si usamos " no hace falta poner \
'''

'''
'''

valor1 = int(input('Escriba valor1: '))
valor2 = int(input('Escriba valor2: '))
if valor1 > valor2:
    print('El valor1 es mayor')
else:
    print('El valor2 es mayor')

'''

