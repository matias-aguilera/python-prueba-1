#escribir una funcion que calcule el area de un circulo y otra que calcule el volumen de un cilindro usando la primera funcion

#Área = π * radio^2
#volumen cilindro = v=pi * r**2 * h

def circulo(radio):
    pi = 3.14
    area = (pi * radio**2)
    return (area)

   

def volumen_cilindro(altura, radio):
    pi = 3.14
    volumen = (circulo(radio) * altura)
    return(volumen)


def main():
   radio=int(input("ingrese el valor del area: "))
   altura=int(input("ingrese el valor de la altura: "))

   print(circulo(radio))
   print(volumen_cilindro(altura, radio))



if __name__=="__main__":
     main()