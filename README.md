# Project Setup and Execution Guide

## Getting Started

### Install Required Libraries
```sh
pip install -r requirement.txt
```

## 🛠️ Bugs Fixed

| File         | Bug                                          | Fix                                            |
|--------------|-----------------------------------------------|------------------------------------------------|
| `agents.py`  | Used `tool=` instead of `tools=`             | ✅ Corrected to `tools=[...]`                  |
| `tools.py`   | Missing import for PDFLoader                 | ✅ Added `from langchain.document_loaders import PDFLoader` |
| `tools.py`   | `read_data_tool` lacked `@staticmethod`      | ✅ Added `@staticmethod`                       |
| `main.py`    | Only used one agent/task                     | ✅ Now runs full team and all tasks in sequence |
| `task.py`    | All tasks used `doctor` only                 | ✅ Each task now uses its corresponding agent  |

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/blood-test-analyser-debug.git
cd blood-test-analyser-debug
```

## Setup Environment Variables
### Create a .env file in the root directory with your OpenAI key:
```ini
OPENAI_API_KEY=your_openai_api_key_here
```

## Usage Instruction
### Run the FastAPI Server  
```bash
uvicorn main:app --reload
```

## API Documentation
GET /
Health check endpoint
Returns:
```json
{ "message": "Blood Test Report Analyser API is running" }
```

POST /analyze
Analyzes a blood test PDF with the help of 4 CrewAI agents.

Form Data Parameters:

file: PDF file (required)

query: Optional text prompt (default: "Summarise my Blood Test Report")



