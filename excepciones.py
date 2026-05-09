class ClienteError(Exception):
    """Excepción base para errores del módulo de clientes."""
    pass
class CampoVacioError(ClienteError):
    """Se lanza cuando un campo obligatorio está vacío."""
    pass
class CedulaInvalidaError(ClienteError):
    """Se lanza cuando la cédula no cumple los requisitos mínimos."""
    pass
class CedulaDuplicadaError(ClienteError):
    """Se lanza cuando ya existe un cliente con la misma cédula."""
    pass