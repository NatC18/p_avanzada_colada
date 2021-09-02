import random
import parametros as p

class Mascota:
    def __init__(self, nombre, raza, dueno, saciedad, entretencion):
        self.nombre = nombre
        self.raza = raza
        self.dueno = dueno
        
        # Los siguientes valores están en %.
        self._saciedad = saciedad
        self._entretencion = entretencion

    # COMPLETAR
    def saciedad(self):
        pass

    # COMPLETAR
    def entretencion(self):
        pass

    @property
    def satisfaccion(self):
        return (self.saciedad//2 + self.entretencion//2)
    
    def comer(self, comida):
        # COMPLETAR
        pass

    def pasear(self):
        self.entretencion += p.ENTRETENCION_PASEAR
        self.saciedad += p.SACIEDAD_PASEAR
    
    def __str__(self):
        # COMPLETAR
        pass


class Perro(Mascota):
    def __init__(self, nombre, raza, dueno, saciedad, entretencion):
        # COMPLETAR
        self.especie = "perro"
        super().__init__(nombre, raza, dueno, saciedad, entretencion)
        pass
    
    def saludar(self):
        # COMPLETAR
        pass
        

class Gato(Mascota):
    def __init__(self, nombre, raza, dueno, saciedad, entretencion):
        # COMPLETAR
        self.especie = "gato"
        super().__init__(nombre, raza, dueno, saciedad, entretencion)
        pass

    def saludar(self):
        # COMPLETAR
        pass

class Conejo(Mascota):
    def __init__(self, nombre, raza, dueno, saciedad, entretencion):
        # COMPLETAR
        self.especie = "conejo"
        super().__init__(nombre, raza, dueno, saciedad, entretencion)
        pass

    def saludar(self):
        # COMPLETAR
        pass
