from fastapi import HTTPException, UploadFile
from llama_index import download_loader
import s3fs
import os

from store.virtualFileSystem.s3_reader import S3Reader


class S3Service:
    def __init__(self):
        self.bucket_name = os.environ.get('GCP_STORAGE_BUCKET_NAME')
        self.access_key = os.environ.get('GCP_STORAGE_ACCESS_KEY')
        self.secret_key = os.environ.get('GCP_STORAGE_SECRET_KEY')
        self.storage_region_name = os.environ.get('GCP_STORAGE_REGION_NAME')

        self.fs = s3fs.S3FileSystem(
            key=self.access_key,
            secret=self.secret_key,
            client_kwargs={
                "region_name": self.storage_region_name
            }
        )

        self.bucket_name = self.bucket_name

    def get_reader(self, path):

        def extract_file_metadata(file_path):
            directory, file_name = os.path.split(file_path)
    
            # Extract client_name and namespace
            parts = directory.split("___")
            sub_parts = parts[-1].split("/")
            
            client_name = sub_parts[0]
            namespace = sub_parts[1]
            
            # Extract file_path
            file_path_from_namespace = "/".join(sub_parts[2:])

            return {
                "client_name": client_name,
                "namespace": namespace,
                "file_path": file_path_from_namespace,
                "file_name": file_name
            }

        return S3Reader(
            bucket=self.bucket_name,
            region_name=self.storage_region_name,
            prefix=path,
            aws_access_id=self.access_key,
            aws_access_secret=self.secret_key,
            file_metadata=extract_file_metadata
        )

    def _upload_file(self, file_name: str, content: bytes, client_name: str, namespace: str, path: str) -> bool:
        try:
            s3_path = self.get_path(client_name, namespace, file_name, path)
            with self.fs.open(s3_path, "wb") as f:
                f.write(content)
            return True
        except Exception as e:
            print(f"Error uploading {file_name} to S3: {e}")
            return False

    async def upload_files(self, files: list[UploadFile], client_name: str, namespace: str, path: str):
        for file in files:
            content = await file.read()
            file_name = file.filename
            result = self._upload_file(
                file_name, content, client_name, namespace, path)
            if not result:
                raise HTTPException(
                    status_code=500, detail="Failed to upload some files to S3")
        return {"status": "uploaded", "name": client_name}

    def get_path(self, client_name: str, space_name: str = None, file_name: str = None, path: str = ''):
        if (space_name is not None and file_name is not None and path is not None):
            return f"s3://{self.bucket_name}/{client_name}/{space_name}/{path}/{file_name}"
        elif (space_name is not None and path is not None):
            return f"s3://{self.bucket_name}/{client_name}/{space_name}/{path}"
        else:
            return f"s3://{self.bucket_name}/{client_name}"
