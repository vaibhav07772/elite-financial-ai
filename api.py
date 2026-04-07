from fastapi import FastAPI, UploadFile
import shutil
from rag import run_rag

app = FastAPI()

@app.post("/analyze")
async def analyze(files: list[UploadFile], query: str):
    
    paths = []
    
    for file in files:
        path = f"data/{file.filename}"
        
        with open(path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        paths.append(path)
    
    answer, ratios = run_rag(paths, query)
    
    return {
        "answer": answer,
        "ratios": ratios
    }