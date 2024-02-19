class Personas:
    def __init__(self, nombre, edad, email=None):
        self._nombre = nombre
        self._edad = edad
        self._email = email

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    def dict(self):
        return {'nombre': self._nombre, 'edad': self._edad, 'email': self._email}

    def __str__(self):
        return f"Persona: {self.dict()}"


class Cliente(Personas):
    def __str__(self):
        return f"Cliente: {self.dict()}"


if __name__ == "__main__":
    persona1 = Personas("Juan", 30)
    print(persona1)

    cliente1 = Cliente("Maria", 25, "maria@example.com")
    print(cliente1)


class Cliente(Personas):
    def __str__(self):
        return f"Cliente: {self.dict()}"


if __name__ == "__main__":
    persona1 = Personas("Juan", 30)
    print(persona1)

    cliente1 = Cliente("Maria", 25, "maria@example.com")
    print(cliente1)