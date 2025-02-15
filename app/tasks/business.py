from typing import Dict, Any
import aiohttp
import sqlite3
import json
from pathlib import Path

DATA_DIR = Path("./data")

async def process_business_task(task: Dict[str, Any]) -> Dict[str, Any]:
    """Handle business tasks like API calls, SQL queries etc"""
    
    task_type = task.get("type")
    
    if task_type == "fetch_api":
        return await fetch_api_data(task)
    elif task_type == "run_sql":
        return await run_sql_query(task)
    elif task_type == "scrape_website":
        return await scrape_website(task)
    else:
        raise ValueError(f"Unknown business task type: {task_type}")

async def fetch_api_data(task: Dict[str, Any]) -> Dict[str, Any]:
    url = task["parameters"].get("url")
    if not url:
        raise ValueError("URL parameter is required")
        
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            
    output_file = DATA_DIR / task["parameters"].get("output", "api_output.json")
    with open(output_file, "w") as f:
        json.dump(data, f, indent=2)
        
    return {"saved_to": str(output_file)}

async def run_sql_query(task: Dict[str, Any]) -> Dict[str, Any]:
    db_path = DATA_DIR / task["parameters"].get("database", "")
    query = task["parameters"].get("query")
    
    if not query:
        raise ValueError("SQL query is required")
        
    conn = sqlite3.connect(str(db_path))
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        return {"results": results}
    finally:
        conn.close()

async def scrape_website(task: Dict[str, Any]) -> Dict[str, Any]:
    url = task["parameters"].get("url")
    selector = task["parameters"].get("selector")
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            html = await response.text()
            
    # TODO: Implement actual scraping logic
    return {"html": html[:1000]}  # Return first 1000 chars for now 