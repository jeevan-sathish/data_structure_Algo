from fastapi import FastAPI ,Request,Response

app=FastAPI(
    title="My FastAPI Application",
    description="This is a sample FastAPI application.",
    version="1.0.0",
    docs_url="/testdocs",
    redoc_url="/redoc",
    debug=True
)

@app.get("/")
async def root_read(request:Request,response:Response):
    print(str(request.url))
    
    response.status_code = 200

    return {"message": "Hello World"}
