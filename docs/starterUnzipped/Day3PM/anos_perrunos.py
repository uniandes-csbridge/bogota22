"""
File: anos_perrunos.py
--------------------
Este programa le pregunte al usuario por una edad humana 
(expresada como un numero entero) y luego imprima el equivalente 
en años caninos, usando el hecho de que hay 7 años caninos en 
un año humano. Considera usar una constante CANINOS_POR_HUMANO. 
"""


def main():
    entrada = int(input("Ingresa una edad en años humanos: "))
    while entrada != 0:
        if entrada < 0:
            print("Disculpa, por favor usa un numero positivo o ingresa 0 para salir del programa.")
        else:
            # TODO: tu código acá 
            pass
        entrada = int(input("Ingresa una edad en años humanos: "))


def calcular_edad_perro(edad_humano):
    """
    Acepte como un parametro un entero llamado edad_humano y 
    retorna la edad humana convertida.

    """
    # TODO: tu código acá
    pass


if __name__ == "__main__":
    main()
