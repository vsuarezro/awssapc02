from fastapi import FastAPI
from datetime import datetime

app=FastAPI()

@app.get("/")
async def root():
    current_date_time = datetime.now().strftime("%Yy-%mm-%dd %H:%M:%S")
    return {"message": "Hello World", "time" : current_date_time}

