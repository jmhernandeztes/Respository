#Jose Hernandez
class Vehiculo:
    def __init__(self, marca, modelo, pais_procedencia, ano_fabricacion, tipo_combustible=None, chasis=None, cilindraje=None):
        self.marca = marca
        self.modelo = modelo
        self.pais_procedencia = pais_procedencia
        self.ano_fabricacion = ano_fabricacion
        self.tipo_combustible = tipo_combustible
        self.chasis = chasis
        self.cilindraje = cilindraje

    def __str__(self):
        return (f"Marca: {self.marca}\n"
                f"Modelo: {self.modelo}\n"
                f"Pais de Procedencia: {self.pais_procedencia}\n"
                f"Año de Fabricación: {self.ano_fabricacion}\n"
                f"Tipo de Combustible: {self.tipo_combustible}\n"
                f"Chasis: {self.chasis}\n"
                f"Cilindraje: {self.cilindraje}")

if __name__ == '__main__':
    mi_vehiculo = Vehiculo('Toyota', 'Corolla', 'Japón', 2020, 'Gasolina', '1234567890', 1800)

    # Imprimir la instancia de Vehiculo
    print(mi_vehiculo)