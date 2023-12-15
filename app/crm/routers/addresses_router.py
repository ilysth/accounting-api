import os
import requests

from dotenv import load_dotenv
from functools import cache
from fastapi import APIRouter
from pathlib import Path

router = APIRouter(prefix="/addresses", tags=["Addresses Resources"])

dotenv_path = Path("env/.env")
load_dotenv(dotenv_path=dotenv_path)
api_key = os.getenv("MAPS_API_KEY")


@router.get("/autocomplete")
async def get_autocomplete_suggestions(input: str):
    base_url = "https://maps.googleapis.com/maps/api/place/autocomplete/json"
    query = {"key": api_key, "input": input}
    response = requests.get(url=base_url, params=query)
    return response.json()


@router.get("/detail")
async def get_place_details(place_id: str):
    base_url = "https://maps.googleapis.com/maps/api/place/details/json"
    query = {
        "key": api_key,
        "place_id": place_id,
        "fields": "address_component,website,formatted_address",
    }
    response = requests.get(url=base_url, params=query)
    return response.json()
