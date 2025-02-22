#brokerCliente.py

import mysql.connector

class BrokerCliente():
    def __init__(self) -> None:## Constructor de la clase
         pass## No se realiza ninguna acción

    def consultar_cliente_id(self, idCliente: str):## Método para consultar un cliente por id
         db = mysql.connector.Connect(
             host="localhost",
             user="root",
             passwd="root",
             db="rappiapp"
         )
         results = []
         try:
            query = (f"SELECT * FROM cliente WHERE idCliente = '{idCliente}'") ##La f antes de la cadena de texto permite la interpolación de variables
            cursor = db.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
            cursor.close()
        
         except Exception as ex:
            results = [f"Consultar Cliente Fallido: {ex}"]
         finally:
            db.close()
         return results
         
         
         
