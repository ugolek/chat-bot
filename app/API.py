from fastapi import FastAPI, File, Form, UploadFile
from core.main_service import MainService
from typing import List
from google.cloud import storage
import os

app = FastAPI()
main_service = MainService()


@app.post("/space/create-space/")
async def create_space(
        client_name: str = Form(...),
        space_name: str = Form(...),
        files: list[UploadFile] = File(...),
        path: str = Form(...)
):
    await main_service.upload_files_to_namespace(files, client_name, space_name, path)
    return {"status": "updated", "name": client_name, space_name: space_name}


@app.post("/space/upload-files/")
async def upload_files_to_space(
        client_name: str = Form(...),
        space_name: str = Form(...),
        files: list[UploadFile] = File(...),
        path: str = Form(...)
):
    await main_service.upload_files_to_namespace(files, client_name, space_name, path)
    return {"status": "updated", "name": client_name, space_name: space_name}


# @app.post("/space/upload/")
# async def upload(client_name: str = Form(...), space_name: str = Form(...),  files: list[UploadFile] = File(...)):
#     await main_service.ask_namespace(files, client_name, space_name)
#     return {"status": "updated", "name": client_name}


@app.post("/space/ask/")
async def ask_index(client_name: str, namespace: str, question: str):
    answer = main_service.ask_namespace(question, namespace)

    return {"status": "ok", "answer": answer}


@app.post("/space/ask_with_retriever/")
async def ask_with_retriever(client_name: str, namespace: str, question: str):
    response = main_service.ask_namespace_with_recursive_retriever(question, namespace)

    return {"status": "ok", "response": response, }


# @app.post("/l_index/")
# async def update_index(l_index_name: str, files: list[UploadFile]):
#     main_service.upload_data(files, l_index_name)
#     return {"status": "updated", "name": l_index_name}


# @app.post("/l_index/create")
# async def create_l_index(l_index_name: str, files: list[UploadFile]):
#     main_service.upload_data(files, l_index_name)
#     return {"status": "updated", "name": l_index_name}


# @app.put("/l_index/")
# async def update_index_by_local(l_index_name: str, path: str):
#     main_service.upload_local_data(path, l_index_name)
#     return {"status": "uploaded", "name": l_index_name}

# @app.post("l_index/uploadfiles")
# async def upload_file(l_index_name: str, files: List[UploadFile] = File(...)):

#     main_service.upload_files(files, l_index_name)

#     return {
#         "filename": new_filename,
#         "content-type": file.content_type
#     }


# @app.post("/ask_question/")
# def ask_question(l_index_name: str, question: str):
#     query = main_service.queryFromCloud(question, l_index_name)
#     return {"status": "created", "answer": query}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
