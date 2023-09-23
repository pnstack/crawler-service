from fastapi import FastAPI
app = FastAPI()

# health check

@app.get("/health")
async def health_check():
    return {"message": "I'm alive"}

import src.modules.news
