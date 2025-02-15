# LLM-based Automation Agent

Ye ek automation agent hai jo plain English tasks ko execute karta hai aur LLM ka use karke multi-step processes ko handle karta hai.

## Features

- POST `/run?task=<task description>` endpoint jo plain English tasks ko execute karta hai
- GET `/read?path=<file path>` endpoint jo file contents return karta hai
- Data directory ke bahar ke files ko access nahi karta
- File system se koi data delete nahi karta

## Installation

Docker image ko run karne ke liye
