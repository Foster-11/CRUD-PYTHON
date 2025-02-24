# main.py

import uvicorn

def start():
    uvicorn.run(
        "api.webApiCliente:app", ## archivo en api que contiene la funcion app
        host="127.0.0.1",
        port=8070,
        reload=True
    )

if __name__ == "__main__":  
    start()
