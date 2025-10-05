from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from predictor import main as run_prediction

app = FastAPI()

# Allow requests from your Flutter app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or restrict to your app domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/predict")
async def predict(request: Request):
    # Receive the dictionary from Flutter
    input_values = await request.json()
    
    # Call your main() function
    result = run_prediction(input_values)
    
    # Return JSON response
    return {"status": "success", "result": result}

@app.get("/")
def root():
    return {"message": "FastAPI is running"}
