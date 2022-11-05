valor = "ADOLFO"
tipo = type(valor)
print(tipo)
if type(valor) == str:
    print("Esto es un string")
elif type(valor) == int:
    print("Esto es un integer")

elif type(valor) == float:
    print("Esto es un float")

elif type(valor) == bool:
    print("Esto es un bool")
