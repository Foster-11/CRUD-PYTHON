from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from model.modeloCliente import modeloCliente
from broker.brokerCliente import BrokerCliente
import logging

app: FastAPI = FastAPI(
    title="web API de Clientes",
    description="crud de clientes"
)

origins = ["*"]  # Permitir solicitudes de cualquier origen

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Permitir solicitudes de cualquier origen
    allow_credentials=True,  # Permitir el envío de credenciales
    allow_methods=["*"],  # Permitir todos los métodos HTTP
    allow_headers=["*"],  # Permitir todos los encabezados
)

# GET
@app.get(
    "/idCliente",
    response_model=list,
    description="Consultar cliente por id",
    summary="Consultar cliente por id",
    tags=["Cliente"]
)
async def get_cliente(idCliente: str):
    broker = BrokerCliente()  
    return broker.consultar_cliente_id(idCliente)  
