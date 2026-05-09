print("Hello, World!")
print("Welcome to the world of programming!")

import logging

from cliente import Cliente
from servicio import ReservaSala
from servicio import AlquilerEquipo
from servicio import AsesoriaEspecializada
from reserva import Reserva

from excepciones import ClienteError
from excepciones import ServicioError

from excepciones import ReservaError


logging.basicConfig(
    filename="errores.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


clientes = []
servicios = []
reservas = []


print("\ SISTEMA DE GESTIÓN SOFTWARE FJ")


# OPERACIÓN 1
try:
    cliente1 = Cliente("Juan Pérez", "juan@gmail.com", "311456789")
    clientes.append(cliente1)
    print("\nCliente registrado correctamente")

except ClienteError as e:
    print(e)
    logging.error(e)   
    
     
# OPERACIÓN 2
try:
    cliente2 = Cliente("", "maria@gmail.com", "320123456")
    clientes.append(cliente2)

except ClienteError as e:
    print(f"Error: {e}")
    logging.error(e)


# OPERACIÓN 3
try:
    cliente3 = Cliente("Carlos", "correo_invalido", "320111111")
    clientes.append(cliente3)

except ClienteError as e:
    print(f"Error: {e}")
    logging.error(e)    
    
    
# OPERACIÓN 4
try:
    sala = ReservaSala("Sala de juntas", 50000)
    servicios.append(sala)
    print("Servicio de sala creado correctamente")

except ServicioError as e:
    print(e)
    logging.error(e)


# OPERACIÓN 5
try:
    equipos = AlquilerEquipo("Computadores", 80000) 
 servicios.append(equipos)
    print("Servicio de equipos creado correctamente")

except ServicioError as e:
    print(e)
    logging.error(e)


# OPERACIÓN 6
try:
    asesoria = AsesoriaEspecializada("Asesoría Python", 120000)
    servicios.append(asesoria)
    print("Servicio de asesoría creado correctamente")

except ServicioError as e:
    print(e)
    logging.error(e)    


# OPERACIÓN 7
try:
    servicio_invalido = ReservaSala("Sala económica", -100)
    servicios.append(servicio_invalido)

except ServicioError as e:
    print(f"Error: {e}")
    logging.error(e)


# OPERACIÓN 8
try:

    reserva1 = Reserva(cliente1, sala, 3)

    try:
        costo = sala.calcular_costo(3, impuesto=0.19)

    except Exception as error_calculo:
        raise ReservaError("Error calculando el costo") from error_calculo  

    reserva1.procesar_reserva()

except ReservaError as e:
    print(f"Error en reserva: {e}")
    logging.error(e)

else:
    reservas.append(reserva1)
    reserva1.mostrar_reserva()
    print(f"Costo total: ${costo}")

finally:
    print("Proceso de reserva finalizado")


# OPERACIÓN 9
try:

    reserva2 = Reserva(cliente1, equipos, -5)   

    reserva2 = Reserva(cliente1, equipos, -5)
    reservas.append(reserva2)

except ReservaError as e:
    print(f"Error: {e}")
    logging.error(e)

finally:
    print("Validación de reserva incorrecta finalizada")


# OPERACIÓN 10
try:

    reserva3 = Reserva(cliente1, asesoria, 2)
    reserva3.cancelar()  
 reserva3.procesar_reserva()

except ReservaError as e:
    print(f"Error: {e}")
    logging.error(e)


print("\n LISTA DE SERVICIOS")

for servicio in servicios:
    print(servicio.descripcion())


print("\n CLIENTES REGISTRADOS")

for cliente in clientes:
    cliente.mostrar_info()
    print("-------------------")     
print("\n RESERVAS EXITOSAS ")

for reserva in reservas:
    reserva.mostrar_reserva()           