#brokerCliente.py

import mysql.connector


class BrokerCliente():
    def __init__(self) -> None:  ## Constructor de la clase
         pass  ## No se realiza ninguna acción

    def consultar_cliente_id(self, idCliente: str) -> list:  ## Método para consultar un cliente por id
         db = mysql.connector.Connect(
             host="localhost",
             user="root",
             passwd="root",
             port="3306",
             db="rappiapp"
         )
         results = []
         try:
            query = "SELECT * FROM cliente WHERE idCliente = %s"  ## Usar parámetros en la consulta
            cursor = db.cursor()
            cursor.execute(query, (idCliente,))  ## Pasar el parámetro idCliente
            results = cursor.fetchall()
            cursor.close()
        
         except Exception as ex:
            results = [f"Consultar Cliente Fallido: {ex}"]
         finally:
            db.close()
         return results



