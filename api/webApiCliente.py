from fastapi import FastAPI
from model.modeloCliente import modeloCliente

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
    broker = BrokerCliente()
    return broker.consultar_cliente_id(id)


#POST
@app.post(
    "/crearCliente",
    response_model= modeloCliente,
    description= "Crear cliente",
    summary="Crear cliente",
    tags=["Cliente"]
)
async def post_cliente(cliente: modeloCliente):
    return cliente

#PUT
@app.put(
    "/actualizarCliente",
    response_model= modeloCliente,
    description= "Actualizar cliente",
    summary="Actualizar cliente",
    tags=["Cliente"]
)
async def put_cliente(parametro: str, cliente: modeloCliente):
    return cliente