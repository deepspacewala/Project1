import os
from pathlib import Path
from typing import Union

DATA_DIR = Path("./data")

async def read_file(file_path: Union[str, Path]) -> str:
    """Safely read files only from data directory"""
    path = Path(file_path)
    
    # Security check
    try:
        full_path = (DATA_DIR / path).resolve()
        if not str(full_path).startswith(str(DATA_DIR.resolve())):
            raise ValueError("Access denied: Can only access files in data directory")
            
        if not full_path.exists():
            raise FileNotFoundError(f"File not found: {path}")
            
        with open(full_path, "r") as f:
            return f.read()
            
    except Exception as e:
        raise ValueError(f"Error reading file: {str(e)}") 