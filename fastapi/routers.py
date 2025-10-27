from fastapi import FastAPI

app=FastAPI()

#Path parameter
@app.get("/items/{item_id}")
def get_item(item_id:int):
    return {"item_id":item_id}
#Query parameter

@app.get("/search")
def search(q:str =None,limit:int =10 ):
    return {"query": q, "limit": limit}  #/search?q=shoes&limit=5 → q = "shoes", limit = 5