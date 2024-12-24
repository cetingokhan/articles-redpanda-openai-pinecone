from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from typing import Dict
import openai
import logging
import json

# OpenAI API Key
openai.api_key = ""


# Logger ayarı
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


# Gelen mesaj modeli
class Message(BaseModel):
    id: str
    email: str
    full_name:str
    content:str

@app.post("/embedding")
async def get_embedding(message: Message):
    logger.info(f"Request Body: {json.dumps(message.id)}")
   
    try:
        # OpenAI embedding işlemi
        response = openai.Embedding.create(
            model="text-embedding-ada-002",
            input=message.content
        )
        embedding = response["data"][0]["embedding"]
                
        result = {
            "id": message.id,
            "email": message.email,
            "full_name": message.full_name,
            "content": message.content,
            "embedding": embedding
        }
        
        logger.info(f"Request Body END: {json.dumps(message.id)}")

        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
