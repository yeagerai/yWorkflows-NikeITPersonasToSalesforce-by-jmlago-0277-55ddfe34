
import os
import requests
from typing import List, Dict, Optional
from pydantic import BaseModel
from fastapi import FastAPI
from dotenv import load_dotenv
from core.abstract_component import AbstractComponent

class FetchNikeITPersonasInputDict(BaseModel):
    AccessToken: str

class FetchNikeITPersonasOutputDict(BaseModel):
    PersonasData: List[Dict]

class FetchNikeITPersonas(AbstractComponent):
    def __init__(self) -> None:
        super().__init__()

    def transform(self, args: FetchNikeITPersonasInputDict) -> FetchNikeITPersonasOutputDict:
        access_token = args.AccessToken
        headers = {"Authorization": f"Bearer {access_token}"}
        url = "https://api.linkedin.com/v2/personas/nike-it-department"
        response = requests.get(url, headers=headers)
        response_data = response.json()
        personas_data = response_data["elements"]

        return FetchNikeITPersonasOutputDict(PersonasData=personas_data)


load_dotenv()
fetch_nike_it_personas_app = FastAPI()


@fetch_nike_it_personas_app.post("/transform/")
async def transform(
    args: FetchNikeITPersonasInputDict,
) -> FetchNikeITPersonasOutputDict:
    fetch_nike_it_personas = FetchNikeITPersonas()
    return fetch_nike_it_personas.transform(args)

