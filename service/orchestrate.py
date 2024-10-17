from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/")
async def test():
    return{
        "response":"this is a simple test of the orchestrator"
    }

# Endpoint en Servicio Orquetador para iniciar la orquestación
@app.get("/orchestrate")
async def orchestrate():
    async with httpx.AsyncClient() as client:
        try:
            respuesta_a = await client.get("http://service-a/test",timeout=1.0)
            data_a = respuesta_a.json()
        except httpx.RequestError:
            data_a = "The service A is not available"

        try:
            respuesta_b = await client.get("http://service-b/test",timeout=1.0)
            data_b = respuesta_b.json()
        except httpx.RequestError:
            data_b = "The service B is not available"
        try:
            respuesta_c = await client.get("http://service-c/test",timeout=1.0)
            data_c = respuesta_c.json()
        except httpx.RequestError:
            data_c = "The service C is not available"
        try:
            respuesta_d = await client.get("http://service-d/test",timeout=1.0)
            data_d = respuesta_d.json()
        except httpx.RequestError:
            data_d = "The service D is not available"
        try:
            respuesta_e = await client.get("http://service-e/test",timeout=1.0)
            data_e = respuesta_e.json()
        except httpx.RequestError:
            data_e = "The service E is not available"
        try:
            respuesta_f = await client.get("http://service-f/test",timeout=1.0)
            data_f = respuesta_f.json()
        except httpx.RequestError:
            data_f = "The service F is not available"

    return {"response_a": data_a,
            "response_b": data_b,
            "response_c": data_c,
            "response_d": data_d,
            "response_e": data_e,
            "response_f": data_f
            }