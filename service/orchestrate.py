from fastapi import FastAPI
import httpx

app = FastAPI()

# Endpoint en Servicio Orquetador para iniciar la orquestación
@app.get("/orquestar")
async def orquestar():
    async with httpx.AsyncClient() as client:
        try:
            respuesta_a = await client.get("http://service-a/servicio-a")
            data_a = respuesta_a.json()
        except httpx.RequestError:
            data_a = "The service A is not available"

        try:
            respuesta_b = await client.get("http://service-b/servicio-b")
            data_b = respuesta_b.json()
        except httpx.RequestError:
            data_b = "The service B is not available"

    return {"response_a": data_a, "response_b": data_b}