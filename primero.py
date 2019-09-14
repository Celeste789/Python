def nombre():
 nombre = input("Ingrese su nombre ")
 print("Hola " + nombre)
 
def itfactorial(n):
 if n ==0:
  return(1)
 else:
  for i in range(n, 1, -1):
   n *= (i - 1)  
  print(n)  

def recFactorial(n):
 if n == 0:
  resultado = 1
  return(resultado)
 else:
  resultado = n * recFactorial(n - 1)
  return(resultado)  

def tabla(x):
 for i in range(0, 11):
  print(x * i) 
 
def palabra():
 x = input("Ingrese una palabra ")
 n = 5
 for i in range(1, n):
  print(x)
  
def rango():
 for i in range(10, 21):
  print(i)
  
def amigos():
 for i in range (1, 6):
  amigo = input("Como se llaman 5 de sus amigos? ")
  print("Hola " + amigo + "!") 
  
def cuantosAmigos():
 n = int(input("Cuantos amigos quiere saludar? "))
 for i in range(1, n + 1):
  amigo = input("Como se llama su amigo? ")
  print("Hola " + amigo + "!") 
  
def pares():
 x = int(input("Ingrese un numero "))
 y = int(input("Ingrese otro numero "))
 for i in range (x, y + 1):
  if i % 2 == 0:
   print(i) 
 
def factorial(n):
 nf = 1
 for n in range(n + 1, 1, -1):
  nf = nf * (n - 1) 
 return(nf)       
   
def todos(i):
 for j in range(i + 1):
  print(str(j) + "-" + str(factorial(j))) 
  
def hola(n):
 for i in range(n):
  print("hola ", end="") 

def saludo(n):
 s = input("Ingrese su saludo ")
 for i in range(n):
  print(s + " ", end="")   
   
