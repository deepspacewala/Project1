from fastapi import FastAPI, HTTPException
from app.task_handler import execute_task
from app.file_manager import read_file
from app.utils.logging import logger
from app.config import settings
import openai

app = FastAPI(title="LLM Automation Agent")

# Initialize OpenAI
openai.api_key = settings.OPENAI_API_KEY

@app.on_event("startup")
async def startup_event():
    """Initialize application on startup"""
    logger.info("Starting LLM Automation Agent")
    # Validate data directory exists
    settings.DATA_DIR.mkdir(exist_ok=True)
    # Additional startup checks can go here

@app.post("/run")
async def run_task(task: str):
    try:
        result = await execute_task(task)
        return {"status": "success", "output": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/read")
async def read_data(path: str):
    try:
        content = await read_file(path)
        return {"content": content}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) 