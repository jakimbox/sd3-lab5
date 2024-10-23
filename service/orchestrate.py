from fastapi import FastAPI,Query
import httpx

app = FastAPI()

@app.get("/")
async def test():
    return{
        "response":"this is a simple test of the orchestrator"
    }

@app.get("/custom")
async def custom(
    path: str = Query("default", description="slaps parameter for service B")
):
    if(path=="default"):
        return{
            "response":"this is a simple test of the custom path"
        }
    else:
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(path,timeout=1.0)
                content_type = response.headers.get("Content-Type")
                if "application/json" in content_type:
                    data = response.json()  # Parse as JSON
                else:
                    data=response.text# Return as plain text
            except httpx.RequestError:
                data = "The path is not available"
            return{
                "data":data
            }

# Endpoint en Servicio Orquetador para iniciar la orquestación
@app.get("/orchestrate")
async def orchestrate():
    async with httpx.AsyncClient() as client:
        try:
            ##"service-a" is the name of the service
            respuesta_a = await client.get("http://service-a/test",timeout=1.0)
            data_a = respuesta_a.json()
        except httpx.RequestError:
            data_a = "The service A is not available"

        try:
            respuesta_b = await client.get("http://service-b/test",timeout=1.0)
            data_b = respuesta_b.text
        except httpx.RequestError:
            data_b = "The service B is not available"
        try:
            respuesta_c = await client.get("http://service-c/test",timeout=1.0)
            data_c = respuesta_c.text
        except httpx.RequestError:
            data_c = "The service C is not available"
        try:
            respuesta_d = await client.get("http://service-d/test",timeout=1.0)
            data_d = respuesta_d.text
        except httpx.RequestError:
            data_d = "The service D is not available"
        try:
            respuesta_e = await client.get("http://service-e/test",timeout=1.0)
            data_e = respuesta_e.text
        except httpx.RequestError:
            data_e = "The service E is not available"
        try:
            respuesta_f = await client.get("http://service-f/test",timeout=1.0)
            data_f = respuesta_f.text
        except httpx.RequestError:
            data_f = "The service F is not available"
        try:
            respuesta_g = await client.get("http://service-g/test",timeout=1.0)
            data_g = respuesta_g.text
            # data_g = "work"
        except httpx.RequestError:
            data_g = "The service G is not here"

    return {"response_a": data_a,
            "response_b": data_b,
            "response_c": data_c,
            "response_d": data_d,
            "response_e": data_e,
            "response_f": data_f,
            "response_g": data_g
            }


## I will only call the service a, developed< by Javier Grijalba
@app.get("/a")
async def serviceA(
    slaps: int = Query(0, description="slaps parameter for service B"),
    slapper: str = Query("jon", description="the one who slaps you")):
    async with httpx.AsyncClient() as client:
        try:
            ##"service-a" is the name of the service
            url = f"http://service-a/slap?slaps={slaps}&slapper={slapper}"
            respuesta_a = await client.get(url,timeout=1.0)
            data_a = respuesta_a.json()
        except httpx.RequestError:
            data_a = "The service A is not available"

        return {"response_a": data_a}
    
## I will only call the service b, developed by
@app.get("/b")
async def serviceB():
    async with httpx.AsyncClient() as client:
        try:
            ##"service-b" is the name of the service
            respuesta_b = await client.get("http://service-b/test",timeout=1.0)
            data_b = respuesta_b.json()
        except httpx.RequestError:
            data_b = "The service B is not available"
        return {"response_b": data_b}


@app.get("/g")
async def serviceG():
    async with httpx.AsyncClient() as client:
        try:
            ##"service-g" is the name of the service
            respuesta_g = await client.get("http://service-g/test",timeout=1.0)
            # data_g = respuesta_g.json()
            data_g = respuesta_g.text
        except httpx.RequestError as e:
            data_g = f"HTTP error occurred: {e}"
        except httpx.HTTPStatusError:
            data_g = f"Error response {respuesta_g.status_code} from service G"
        return {"response_g": data_g}
