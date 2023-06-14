class Herramientas: 
    def __init__(self, lista_numeros):
        self.lista = lista_numeros

    def verifica_primo(self, nro):
        es_primo = True
        for i in range(2,nro):
            if nro % i == 0:
                es_primo = False
                break
        return es_primo
    
    def valor_modal(self, lista, menor):
        lista_unicos = []
        lista_repeticiones = []
        if len(lista) == 0:
            return None
        if (menor):
            lista.sort()
        else:
            lista.sort(reverse=True)
        for elemento in lista:
            if elemento in lista_unicos:
                i = lista_unicos.index(elemento)
                lista_repeticiones[i] +=1
            else:
                lista_unicos.append(elemento)
                lista_repeticiones.append(1)
        moda = lista_unicos[0]
        maximo = lista_repeticiones[0]
        for i , elemento in enumerate(lista_unicos):
            if lista_repeticiones > maximo:
                moda = lista_unicos[i]
                maximo = lista_repeticiones[i]
        return moda, maximo
    
    def conversion_grados(self,valor, origen, destino):
        valor_destino = None
        if origen == "celsius":
            if destino == "celsius":
                valor_destino = valor
            elif destino == "farenheit":
                valor_destino = (valor * 9 / 5) + 32
            elif destino == "kelvin":
                valor_destino = valor + 273.15
            else:
                print("parametro de destino incorrecto")
        elif origen == "farenheit":
            if destino == "celsius":
                valor_destino = (valor - 32) * 5 / 9
            elif destino == "farenheit":
                valor_destino = valor
            elif destino == "kelvin":
                valor_destino = ((valor - 32) * 5 / 9) + 273.15
            else:
                print("parametro de destino incorrecto")
        elif origen == "kelvin":
            if destino == "celsius":
                valor_destino = valor - 273.15
            elif destino == "farenheit":
                valor_destino = ((valor - 273.15)* 9 / 5) + 32
            elif destino == "kelvin":
                valor_destino = valor
            else:
                print("parametro de destino incorrecto")
        else:
            print("parametro de origen incorrecto")
        return valor_destino
    
    def factorial(self,numero):
        if type(numero) != int or numero < 0:
            return None
        elif numero <= 1:
            return 1

        numero = numero * factorial(numero - 1)
        return numero