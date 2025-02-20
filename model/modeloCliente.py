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
    activo: int

    def cliente_helper(cliente):
        return{
            "idCliente": str(cliente['idCliente']),
            "primerNombre": str(cliente['primerNombre']),
            "segundoNombre": str(cliente['segundoNombre']),
            "primerApellido": str(cliente['primerApellido']),
            "segundoApellido": str(cliente['segundoApellido']),
            "email": str(cliente['email']),
            "contrasena": str(cliente['contrasena']),
            "direccion": str(cliente['direccion']),
            "telefono": str(cliente['telefono']),
            "idTipoIdentificacion": int(cliente['idTipoIdentificacion']),
            "fechaRegistro": datetime(cliente['fechaRegistro']),
            "activo": int(cliente['activo'])
        }