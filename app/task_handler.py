from typing import Dict, Any
import openai
from app.tasks.operations import process_operations_task
from app.tasks.business import process_business_task
import os
import json
from config import settings  # We'll create this

async def execute_task(task_description: str) -> Dict[str, Any]:
    # Parse task using GPT-4o-Mini
    parsed_task = await parse_task_with_llm(task_description)
    
    # Route to correct handler
    if parsed_task["category"] == "operations":
        return await process_operations_task(parsed_task)
    elif parsed_task["category"] == "business":
        return await process_business_task(parsed_task)
    else:
        raise ValueError(f"Unknown task category: {parsed_task['category']}")

async def parse_task_with_llm(task_description: str) -> Dict[str, Any]:
    """Use GPT-4o-Mini to parse natural language into structured task"""
    try:
        response = await openai.ChatCompletion.acreate(
            model="gpt-4",  # Replace with actual GPT-4o-Mini model ID
            messages=[
                {"role": "system", "content": """
                Parse the task into a structured format with these fields:
                - category: 'operations' or 'business'
                - type: specific task type
                - parameters: dict of required parameters
                """},
                {"role": "user", "content": task_description}
            ],
            temperature=0.1
        )
        
        parsed = response.choices[0].message.content
        # Add validation here
        return json.loads(parsed)
        
    except Exception as e:
        raise ValueError(f"Failed to parse task: {str(e)}") 