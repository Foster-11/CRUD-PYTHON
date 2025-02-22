from fastapi import FastAPI
from model.modeloCliente import modeloCliente ##Del archivo modeloCliente.py se está importando la clase modeloCliente que contiene la estructura de los datos relacionados con el cliente

from broker.brokerCliente import BrokerCliente ##Del archivo brokerCliente.py se está importando la clase BrokerCliente que contiene los métodos para realizar las operaciones CRUD de los clientes

app: FastAPI = FastAPI(
    title="web API de Clientes",
    description="crud de clientes"
)

#GET
@app.get(
    "/idCliente",
    response_model= list,
    description= "Consultar cliente por id",
    summary="Consultar cliente por id",
    tags=["Cliente"]
)
async def get_cliente(idCliente: str):
    broker = BrokerCliente()##Se crea una instancia de la clase BrokerCliente
    return broker.consultar_cliente_id(id)


#POST
# @app.post(
#     "/crearClientes",
#     response_model= modeloCliente,
#     description= "Crear cliente",
#     summary="Crear cliente",
#     tags=["Cliente"]
# )
# async def post_cliente(cliente: modeloCliente):
#     return cliente

#PUT
# @app.put(
#     "/actualizarCliente",
#     response_model= modeloCliente,
#     description= "Actualizar cliente",
#     summary="Actualizar cliente",
#     tags=["Cliente"]
# )
# async def put_cliente(parametro: str, cliente: modeloCliente):
#     return modeloCliente

#DELETE
# @app.delete(
#     "/eliminarCliente",
#     response_model= modeloCliente,
#     description= "Eliminar cliente",
#     summary="Eliminar cliente",
#     tags=["Cliente"]
# )