from typing import Union
from fastapi import FastAPI
from model import compute_surface_score

app = FastAPI()

@app.get("/surface")
def surface():
    score = compute_surface_score()
    return {"surface": score}
