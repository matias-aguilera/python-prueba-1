#En una determinada empresa, sus empleados son evaluados al final de cada año. 
#Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, 
#traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, 
#pero no valores intermedios entre las cifras mencionadas. 
#A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. 
#La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel. Vea la imagen adjunta.(10 puntos)

#def ecuacion(puntos):
 #   if puntos == 0:
  #       (2400 * 0)
   # elif puntos == 4:
    #    (2400 * 0,4)
    ##elif puntos == 6:
      #  (2400 * 0,6)
    #else:
        #print ("porfavor califique solo con los los numeros 0, 0.4 y 0.6")
    
    

#def main():
    #print ("el saldo es de :"  puntos)


#if __name__=="__main__":
     #main()



def bono(sueldo):

puntos = int(input("¿inserte uo de los 3 valores: 0, 4, 6 "))
if puntos == 0:
    sueldo = (2400 * 0)
elif puntos == 4:
    sueldo = (2400 * 0.4)
elif puntos == 6:
    sueldo =(2400 * 0.6)
else :
    print("eliga una de las opciones mostradas (0, 4, 6)") 
       
    

print("su sueldo en euros es: "  ,sueldo)


    