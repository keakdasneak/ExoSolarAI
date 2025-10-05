from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from predictor import main as run_prediction
from pydantic import BaseModel

app = FastAPI()

# Allow requests from your Flutter app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or restrict to your app domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define expected input structure to be able to
# Input Testdata via FastAPI
class InputValues(BaseModel):
    pl_orbper: float
    pl_orbpererr1: float
    pl_orbpererr2: float
    pl_orbperlim: float
    pl_rade: float
    pl_radeerr1: float
    pl_radeerr2: float
    pl_radelim: float
    pl_radj: float
    pl_radjerr1: float
    pl_radjerr2: float
    pl_radjlim: float
    st_teff: float
    st_tefferr1: float
    st_tefferr2: float
    st_tefflim: float
    st_rad: float
    st_raderr1: float
    st_raderr2: float
    st_radlim: float
    ra: float
    dec: float
    sy_dist: float
    sy_disterr1: float
    sy_disterr2: float
    sy_vmag: float
    sy_vmagerr1: float
    sy_vmagerr2: float
    sy_kmag: float
    sy_kmagerr1: float
    sy_kmagerr2: float
    sy_gaiamag: float
    sy_gaiamagerr1: float
    sy_gaiamagerr2: float

    # To automatically insert test data in FastAPI:
    class Config:
        json_schema_extra = {
            "example": {
                "pl_orbper": 21.1791,
                "pl_orbpererr1": 0.0030,
                "pl_orbpererr2": -0.0027,
                "pl_orbperlim": 0.0,
                "pl_rade": 2.71,
                "pl_radeerr1": 0.33,
                "pl_radeerr2": -0.37,
                "pl_radelim": 0.0,
                "pl_radj": 0.242,
                "pl_radjerr1": 0.029,
                "pl_radjerr2": -0.033,
                "pl_radjlim": 0.0,
                "st_teff": 5277.0,
                "st_tefferr1": 94.9,
                "st_tefferr2": -92.63,
                "st_tefflim": 0.0,
                "st_rad": 1.362,
                "st_raderr1": 0.137,
                "st_raderr2": -0.039,
                "st_radlim": 0.0,
                "ra": 205.8941425,
                "dec": -16.6906686,
                "sy_dist": 569.102,
                "sy_disterr1": 15.007,
                "sy_disterr2": -14.268,
                "sy_vmag": 13.091,
                "sy_vmagerr1": 0.114,
                "sy_vmagerr2": -0.114,
                "sy_kmag": 11.309,
                "sy_kmagerr1": 0.021,
                "sy_kmagerr2": -0.021,
                "sy_gaiamag": 12.8021,
                "sy_gaiamagerr1": 0.000325,
                "sy_gaiamagerr2": -0.000325
            }
        }

@app.post("/predict")
async def predict(input_values: InputValues):
    result = run_prediction(input_values.dict())
    
    # Return JSON response
    return {"status": "success", "result": result}

@app.get("/")
def root():
    return {"message": "FastAPI is running"}
