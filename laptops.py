import uuid

# Construcción del constructor de la app computadoras.
red= 1234
class Computadora:
    def __init__(self, color, procesador, pulgadas, cantidad_rom, cantidad_ram):
        self.color = color
        self.procesador = procesador
        self.pulgadas = pulgadas
        self.cantidad_rom = cantidad_rom
        self.cantidad_ram = cantidad_ram
        pass
    
    # Definición del método call.
    def __call__(self):
        return (f"los datos de la laptop son: Color: {self.color}, Procesador: {self.procesador}, Pulgadas: {self.pulgadas}, Cantidad de RAM: {self.cantidad_ram}, Cantidad de ROM: {self.cantidad_rom}")
    
    def conectar_a_wifi(self, red, serial):
        print(f"Conectando a la red... {red}, con el serial... {serial}")
        
laptop_15 = Computadora(
    color = "Space Gray",
    procesador = "i5",
    pulgadas = "15",
    cantidad_ram= "1024mb",
    cantidad_rom= "1tb"
)

laptop_16 = Computadora(
    color = "black",
    procesador = "i6",
    pulgadas = "16",
    cantidad_ram= "1300mb",
    cantidad_rom= "1tb"
)

def generar_serial_red():
    serial = uuid.uuid4 ()
    return str(serial)

serial_red = generar_serial_red()

print(laptop_15())
print(laptop_16())

laptop_15.conectar_a_wifi(red, serial_red)