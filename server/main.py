from fastapi import FastAPI ,HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
import json
import httpx
from groq import AsyncGroq ,RateLimitError,APIError
from pydantic import BaseModel,StrictInt,ValidationError

load_dotenv()

API_KEY =os.getenv("OPENAI_API_KEY")

app=FastAPI(
    title="My FastAPI Application",
    description="This is a sample FastAPI application.",
    version="1.0.0",
    docs_url="/testdocs",
    redoc_url="/redoc",
    debug=True
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ResponseModel(BaseModel):
      name:str
      age:StrictInt
      school:str

      
with open("data.json" ,"r") as file:
        student_data = json.load(file)


@app.post("/{id}")
async def root_read(id:int):
    
    student = [s for s in student_data if s["id"]== id ]
    if(student):
          return student
    raise HTTPException(
          status_code =404,
          detail =f"student not found with id {id}"
    )


@app.get("/res" , response_model =ResponseModel)
def demo_res():
      data =  {
                              "name":"jeevan",
                              "age":"22",
                              "school":"stjoseph"
                        }
      try:
            return ResponseModel.model_validate(data)
      except ValidationError as e:
            raise HTTPException(
                  status_code =5000,
                  detail="validation error"
            )from e




app = FastAPI()

@app.get("/external")
async def call_ext():
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(
                "https://jsonplaceholder.typicode.com/comments"
            )
            response.raise_for_status()
            return response.json()

    except httpx.HTTPError as e:
        raise HTTPException(
            status_code=502,
            detail="External API failed"
        ) from e


    
class Prompt(BaseModel):
     prompt:str




from groq import (
    AsyncGroq,
    RateLimitError,
    APIStatusError,
    APIConnectionError,
)

client = AsyncGroq(api_key=os.getenv("GROQ_API_KEY"))

@app.post("/chat", tags=["chat"])
async def chat_now(prompt: Prompt):
    try:
        response = await client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {"role": "user", "content": prompt.prompt}
            ],
            max_completion_tokens=150
        )

        return {
            "question": prompt.prompt,
            "answer": response.choices[0].message.content
        }

    except RateLimitError as e:
        print("Groq rate limit:", repr(e))
        raise HTTPException(
            status_code=429,
            detail="Too many requests or API quota exceeded"
        ) from e

    except APIConnectionError as e:
        print("Groq connection error:", repr(e))
        raise HTTPException(
            status_code=503,
            detail="Unable to connect to AI service"
        ) from e

    except APIStatusError as e:
        print("Groq API status:", e.status_code, repr(e))
        raise HTTPException(
            status_code=502,
            detail="AI service request failed"
        ) from e



class Bulk(BaseModel):
     items:list[str]


@app.post('/bulk')
def bul_response(item:Bulk,query:str):
     length =len(item.items)
     uper_items =[i.upper() for i in item.items]
     result =query in item.items
     
          

     return {
          "items":item.items,
          "size":length,
          "upper_coce":uper_items,
          "result":result
     }
    
     
     