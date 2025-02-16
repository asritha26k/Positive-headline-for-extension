import os
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from model_loader import predict

app = FastAPI()

# Add CORS middleware to allow requests from your Chrome extension
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can specify a list of allowed origins here for security
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Root endpoint to check if API is working
@app.get("/")
def read_root():
    return {"message": "API is working!"}

class InputText(BaseModel):
    text: str

@app.post("/predict/")
def get_prediction(input_data: InputText):
    result = predict(input_data.text)
    return {"modified_text": result}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
