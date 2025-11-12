from fastapi import FastAPI
from pydantic import BaseModel


app=FastAPI()


class filter_schema(BaseModel):
    data : list
    threshold : int



@app.post("/filter")
async def filter(filter_schema) -> int:
    return [x for x in filter_schema.data if x>filter_schema.threshold]

