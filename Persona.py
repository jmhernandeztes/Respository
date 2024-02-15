#Jose Hernandez
class Persona:
    '''
    Crear los objetos de tipo Persona
    '''
    def init(self, nombre, genero, ocupacion=None): #metodo que inicializa al objeto de tipo persona (constructor)
        self._nombre = nombre
        self._genero = genero
        self._ocupacion = ocupacion

    def str(self): #downders son sobre escritos
        return (f'Persona: [nombre: {self._nombre}, genero: {self._genero}, '
                f'ocupación: {self._ocupacion}]')

    def saludar(self):
        print(f'Hola soy {self.nombre}')


if "name" == '_main':
    obj_persona1 = Persona('Luis', 'M', 'Estudiante')
    print(obj_persona1.str())
    obj_persona2 = Persona(genero='F', ocupacion='Tecnolog', nombre='Maria')
    print(obj_persona2)
    p3 = Persona(nombre='Jose', genero='M')
    print(p3)
    obj_persona1.saludar()