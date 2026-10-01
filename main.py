from fastapi import FastAPI

app = FastAPI()

ITEMS = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"},
]

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/items")
def items():
    return ITEMS
