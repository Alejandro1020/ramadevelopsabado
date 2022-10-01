#2.	Función lambda que clasifique números mayores a 10 en una lista


Clasificar2=lambda numero : numero>10

list=[1,5,4]

for numero in list:
    
    if(Clasificar2(numero)):
        print("Es mayor")
    else:
        print("es menor ")    
