from typing import Union
from routers import api
from fastapi import FastAPI

app = FastAPI()

app.include_router(api.router, prefix="/api/v1", tags=["api"])

if __name__ == "__main__":
	import uvicorn
 

	uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
