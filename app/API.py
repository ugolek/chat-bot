from fastapi import FastAPI
from core.main_service import MainService

app = FastAPI()
main_service = MainService()


@app.put("/l_index/")
def update_index(l_index_name: str, data: dict):
    main_service.upload_data(data, l_index_name)
    return {"status": "updated", "name": l_index_name}

@app.put("/l_index/")
def update_index_by_local(l_index_name: str, path: str):
    main_service.upload_local_data(path, l_index_name)
    return {"status": "uploaded", "name": l_index_name}


@app.post("/ask_question/")
def ask_question(l_index_name: str, question: str):
    query = main_service.queryFromCloud(question, l_index_name)
    return {"status": "created", "answer": query}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
