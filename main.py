from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from model_loader import predict  # Import directly from model_loader.py

app = FastAPI()

# Add CORS middleware to allow requests from your Chrome extension
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all domains for now, or specify your extension's URL
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
