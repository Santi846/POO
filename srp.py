# OLD - sin SRP

class ViejoAuto():
    def __init__(self):
        self.posicion = 0
        self.combustible = 100
    
    def mover(self, distancia):
        if(self.combustible >= distancia /2):
            self.posicion += distancia
            self.combustible -= distancia
        else:
            print("No hay suficiente combustible")

    def agregar_combustible(self, cantidad):
        self.combustible += cantidad
    
    def obtener_combustible(self):
        return self.combustible
    
# Single Responsability Principle

class Auto():
    # pasamos el objeto (instancia de la otra clase) como parametro, para asi acceder a sus metodos, y aplicarlos sobre nuestro atributo
    def __init__(self, tanque):
        self.posicion = 0
        # indicamos que el valor de nuestro atributo, es el objeto pasado por parametro
        self.tanque = tanque
    
    def mover(self, distancia):
        if(self.tanque.obtener_combustible() >= distancia / 2):
            self.posicion += distancia
            self.tanque.usar_comnbustible(distancia / 2)
            print(f"Haz movido el auto exitosamente con: {self.tanque.combustible} ")
        else:
            print("No hay suficiente combustible")
    
    # requiere retorno por estar dentro de un print, para no devolver null
    def obtener_posicion(self):
        if(self.posicion > 0):
            print("Lo moviste a la posicion: ")
            return self.posicion
        else:
            print("Partiendo de la posicion inicial")
            return self.posicion
class TanqueCombustible():
    def __init__(self):
        self.combustible = 100

    def agregar_combustible(self, cantidad):
        self.combustible += cantidad

    def usar_comnbustible(self, cantidad):
        self.combustible -= cantidad

    def obtener_combustible(self):
        return self.combustible
    
tanque = TanqueCombustible()
# composicion => tanque compone a auto
autito = Auto(tanque)

# ejecucion de metodos 

print(autito.obtener_posicion())
autito.mover(10)

print(autito.obtener_posicion())
autito.mover(20)

print(autito.obtener_posicion())
autito.mover(60)

print(autito.obtener_posicion())
autito.mover(100)


print(autito.obtener_posicion())
autito.mover(100)
