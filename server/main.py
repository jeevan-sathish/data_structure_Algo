from fastapi import FastAPI ,HTTPException
from fastapi.middleware.cors import CORSMiddleware
import json
import httpx
from pydantic import BaseModel,StrictInt,ValidationError

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
