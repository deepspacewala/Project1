from typing import Dict, Any
import subprocess
from pathlib import Path
from datetime import datetime
import json

DATA_DIR = Path("./data")

async def process_operations_task(task: Dict[str, Any]) -> Dict[str, Any]:
    """Handle operations tasks like formatting, log processing etc"""
    
    task_type = task.get("type")
    
    if task_type == "format_md":
        return await format_markdown(task)
    elif task_type == "count_wednesdays":
        return await count_wednesdays(task)
    elif task_type == "process_logs":
        return await process_logs(task)
    else:
        raise ValueError(f"Unknown operations task type: {task_type}")

async def format_markdown(task: Dict[str, Any]) -> Dict[str, Any]:
    file_path = DATA_DIR / task["parameters"].get("file", "")
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
        
    subprocess.run(["npx", "prettier", "--write", str(file_path)])
    return {"formatted_file": str(file_path)}

async def count_wednesdays(task: Dict[str, Any]) -> Dict[str, Any]:
    file_path = DATA_DIR / task["parameters"].get("file", "")
    with open(file_path, "r") as f:
        dates = [datetime.strptime(line.strip(), "%Y-%m-%d") for line in f]
    
    wednesday_count = sum(1 for d in dates if d.weekday() == 2)
    return {"wednesday_count": wednesday_count}

async def process_logs(task: Dict[str, Any]) -> Dict[str, Any]:
    file_path = DATA_DIR / task["parameters"].get("file", "")
    pattern = task["parameters"].get("pattern", "ERROR")
    
    with open(file_path, "r") as f:
        matching_lines = [line for line in f if pattern in line]
        
    return {"matches": matching_lines} 