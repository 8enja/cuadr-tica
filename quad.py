import math
def redondeo(x):
    if x % 1 == 0:          # si x es entero, no tendrá punto flotante; si no es entero, tendrá sólo dos decimales
        x = int(x)
    else:
        x = round(x, 2) 
    return x

def signo_de_mas(x):        # en la comprobación(), vamos a representar la suma de los tres valores
    if x < 0:               # si el valor es positivo, se agrega el carácter "+" para representar el signo en la suma
        return ""           # si el valor es negativo, sólo se deja un espacio en blanco, pues el valor ya tiene su propio signo
    else:
        return "+"

def comprobacion(x,a,b,c):
    ax = redondeo(a*(pow(x,2)))
    bx = redondeo(b*x)
    print("(",a, "* (",redondeo(x),"^2) )","+ (",b,"*",redondeo(x),") + (",c,") = 0")
    print(ax, signo_de_mas(bx), bx, signo_de_mas(c), c, "=", redondeo(ax + bx + c))

def cuadratica():
    print("############### ECUACIÓN CUADRÁTICA ###############")
    
    while True:
        try:
            print("Ingresa los valores de A, B y C separados por espacios")
            print("Para salir, escribe 'x'")
            entrada = input("> ")               
            if entrada == "X" or entrada == "x":
                break
            else:
                print()
                numeros = entrada.split()
                
                #print("a=", a, ", b=", b, ", c=", c,"\n", sep="")
                if len(numeros) != 3:
                    print("Ingresa 3 números")
                    print("##########\n")
                else:
                    a = int(numeros[0])
                    b = int(numeros[1])
                    c = int(numeros[2])
                    radicando =  pow(b,2) - (4*a*c)

                    if radicando < 0:
                        print("La ecuación no tiene una solución")
                        print("##########\n")
                        
                    elif radicando == 0:
                        x = -b / (2*a) 
                        print("x = ", redondeo(x))

                        print("\n Comprobación:\n")
                        comprobacion(x,a,b,c)
                        print("##########\n")

                    else:
                        x1 = (-b + math.sqrt(radicando)) / (2*a)             
                        x2 = (-b - math.sqrt(radicando)) / (2*a)           
                            
                        print("x1 = ", redondeo(x1))
                        print("x2 = ", redondeo(x2))

                        print("\n Comprobación:\n")
                        comprobacion(x1,a,b,c)
                        print()
                        comprobacion(x2,a,b,c)
                        print("##########\n")
                #break
                    
        except ValueError:                      # si escribe letras o caracteres especiales
            print("Sólo se aceptan números\n")    

        #except IndexError:                     # si sólo escribe uno o dos valores
        #    print("Ingresa 3 valores\n")       
        
        except ZeroDivisionError:               # si el primer valor, "a", es 0
            print("No es una ecuación cuadrática\n")
            #break
     
        
cuadratica()
        
# IndexError
# ZeroDivisionError
# ValueError   
