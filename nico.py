import csv
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m' 
BLUE = '\033[34m'
RESET = '\033[0m' 
print(RED + "reprobado" + RESET)








def agregar(info):
    print("_____________________________________")
    rut=input("escribe el rut del estudiante: ")
    print("_____________________________________")
    nombre=input("escribe el nombre del estudiante: ")
    print("_____________________________________")
    info[rut]=nombre
    print("_____________________________________")
    nota1=input("escribe la primera nota: ")
    print("_____________________________________")
    nota2=input("escribe la segunda nota: ")
    print("_____________________________________")
    nota3=input("escribe la tercera nota: ")
    print("_____________________________________")
    nota4=input("escribe la cuarta nota: ")
    print("_____________________________________")
    
    

    info[rut]={
        'rut':rut,
        'nombre':nombre,
        'nota 1':nota1,
        'nota 2':nota2,
        'nota 3':nota3,
        'nota 4':nota4,
    }


def visualizar(info):
    print("____________________________________________________")
    rut=input("escribe el rut del estudiante que quieres buscar")
    print("____________________________________________________")
    if rut in info:
        print(info)
    else:
        print("estudiante no valido")        

def calculo(info):
    print("_____________________________________")
    rut=input("escribe el rut del estudiante: ")
    print("_____________________________________")
    if rut in info:
        print(info)
        print("_____________________________________")
        suma1=input("ingresa la primera nota: ")
        print("_____________________________________")
        suma2=input("ingresa la segunda nota: ")
        print("_____________________________________")
        suma3=input("ingresa la tercera nota: ")
        print("_____________________________________")
        suma4=input("ingresa la cuarta nota: ")
        print("_____________________________________")        
        resultado=suma1+suma2
        resultado+suma3
        resultado+suma4
        resultado=float(resultado)
        division=resultado/4
        print("_____________________________________")
        print("este es el promedio",division)
        print("_____________________________________")
    else:
        print("estudiante no encontrado")
def aprobar(info):
    nombre=input("escribe el rut del estudiante que aprobo: ")
    if nombre in info:
        print("el estudiante esta",nombre)
        print(GREEN + "aprobado" + RESET)
        info[nombre]={
          'estudiante aprobado':nombre  
        }
    else:
        print("escribe un nombre valido")
def desaprobar(info):
    nombre=input("escribe el rut del estudiante que aprobo: ")
    if nombre in info:
        print("el estudiante el estudiante esta",nombre)
        print(RED + "desaprobado" + RESET)
        info[nombre]={
          'estudiante desaprobado':nombre  
        }
    else:
        print("escribe un nombre valido")

def ver(info):
    print(info)                      
def menu():
    info={}
    while True:
        print("__________________________")
        print("1- agregar estudiante")
        print("2- buscar estudiante")
        print("3- calcular notas")
        print("4- aprobar estudiantes")
        print("5- desaprobar estudiantes")
        print("6- ver todos")
        print("7- salir")
        print("__________________________")
        ops=input("selecciona una opcion: ")
        print("__________________________")
        if ops =="1":
            agregar(info)
        elif ops =="2":
            visualizar(info)
        elif ops =="3":
            calculo(info)
        elif ops=="4":
            aprobar(info)
        elif ops=="5":
            desaprobar(info)
        elif ops=="6":
            ver(info)          
        elif ops =="7":
            print("adios")
            break
        else:
            print("selecciona una opcion valida")
if __name__=="__main__":
    menu()                





