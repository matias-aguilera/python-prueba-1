

#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla,
# el día, el mes y el año como pmuestra la imagen. (10 puntos)


def main():
    fecha = (input("ingrese fecha de nacimiento en formato dd/ mm/aaaa "))
    print("dia ", fecha[0:2]) 
    print("mes", fecha[3:5]) 
    print("año ", fecha[6:10]) 



if __name__=="__main__":
     main()