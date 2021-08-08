from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root_endpoint():
    return {"Hello": "World"}
