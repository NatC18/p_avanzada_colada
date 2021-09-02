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
    #def saciedad(self):
   #     pass

    # COMPLETAR
    #def entretencion(self):
     #   pass

    @property
    def satisfaccion(self):
        return (self._saciedad//2 + self._entretencion//2)
    
    def comer(self, comida):
        # COMPLETAR
        calc = random.random()
        if calc < comida.probabilidad_vencer:
            self.s_aciedad -= comida.calorias
            print(f"La comida estaba vencida! A {self.nombre} le duele la pancita :(")
        else:
            self._saciedad += comida.calorias
            print(f"{self.nombre} está comiendo {comida.nombre}, que rico!")
        pass

    def pasear(self):
        self._entretencion += p.ENTRETENCION_PASEAR
        self._saciedad += p.SACIEDAD_PASEAR
    
    def __str__(self):
        # COMPLETAR
        string = (f"Nombre: {self.nombre}\nSaciedad: {self._saciedad}\nEntretención: {self._entretencion}\nSatisfacción: {self.satisfaccion}")
        return string
        pass


class Perro(Mascota):
    def __init__(self, nombre, raza, dueno, saciedad, entretencion):
        # COMPLETAR
        self.especie = "PERRO"
        super().__init__(nombre, raza, dueno, saciedad, entretencion)
        pass
    
    def saludar(self):
        # COMPLETAR
        print("guau guau")
        pass
        

class Gato(Mascota):
    def __init__(self, nombre, raza, dueno, saciedad, entretencion):
        # COMPLETAR
        self.especie = "GATO"
        super().__init__(nombre, raza, dueno, saciedad, entretencion)
        pass

    def saludar(self):
        # COMPLETAR
        print("miau miau")
        pass

class Conejo(Mascota):
    def __init__(self, nombre, raza, dueno, saciedad, entretencion):
        # COMPLETAR
        self.especie = "CONEJO"
        super().__init__(nombre, raza, dueno, saciedad, entretencion)
        pass

    def saludar(self):
        # COMPLETAR
        print("chillidos")
        pass
