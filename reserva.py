from excepciones import ReservaError

clase reserva
class Reserva:

    def __init__(self, cliente, servicio, cantidad):

        if cantidad <= 0:
            raise ReservaError("La cantidad debe ser mayor que cero")

        self.cliente = cliente
        self.servicio = servicio
        self.cantidad = cantidad
        self.estado = "Pendiente"

    def confirmar(self):
        self.estado = "Confirmada"

    def cancelar(self):
         self.estado = "Cancelada"

    def procesar_reserva(self):

        if self.estado == "Cancelada":
            raise ReservaError("No se puede procesar una reserva cancelada")

        self.confirmar()

    def mostrar_reserva(self):

        print("\n RESERVA")
        print(f"Cliente: {self.cliente.get_nombre()}")
        print(f"Servicio: {self.servicio.nombre}")
        print(f"Cantidad: {self.cantidad}")
        print(f"Estado: {self.estado}")