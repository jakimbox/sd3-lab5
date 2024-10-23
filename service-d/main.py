from fastapi import FastAPI

app = FastAPI()

@app.get("/test")
def read_cachetada():
    return {
        "saludo": "servicio d, te entrega una salchipapita"
    }
