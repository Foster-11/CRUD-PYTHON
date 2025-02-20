#modeloCliente.py

from pydantic import BaseModel
from datetime import datetime

class modeloCliente(BaseModel):
    idCliente: str
    primerNombre: str
    segundoNombre: str
    primerApellido: str
    segundoApellido: str
    email: str
    contrasena: str
    direccion: str
    telefono: str
    idTipoIdentificacion: int
    fechaRegistro: datetime
    activo: bool

    