from fastapi import FastAPI
from collection_manager import CollectionManager
from main_service import MainService
from storage.local_storage import LocalStorage

app = FastAPI()
collection_manager = CollectionManager()
local_storage = LocalStorage()
main_service = MainService()

@app.get("/collections/")
def read_collection():
    names = collection_manager.get_collections()
    return {"names": names, "count": len(names)}

@app.get("/collection/{name}")
def read_collection(name: str):
    collection = collection_manager.get_collection(name)
    return {"name": name, "collection": collection}

@app.post("/collection/")
def create_collection(name: str):
    collection_manager.create_collection(name)
    return {"status": "created", "name": name}

@app.put("/collection/{name}/{path}")
def update_collection(name: str, path: str):
    local_storage.upload_data(path, name)
    return {"status": "updated", "name": name}

@app.delete("/index/{name}")
def delete_collection(name: str):
    collection_manager.delete_collection(name)
    return {"status": "deleted", "name": name}




@app.post("/ask_question/")
def create_collection(collectionName: str, question: str):
    query = main_service.query(question, collectionName)
    return {"status": "created", "answer": query}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
