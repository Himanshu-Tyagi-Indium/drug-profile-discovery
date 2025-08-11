import os
import requests
from fastapi import FastAPI, Query
from openai import AzureOpenAI
from config import LANREOTIDE_SCHEMA,azure_conf

from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_URL = os.getenv("OPENAI_API_URL")

print(azure_conf)


@app.get("/drug-profile")
def get_drug_profile(drug_number: str = Query(..., description="Drug identifier like NDC or NDA")):
    """
    Given a drug number, query GPT with the strict JSON schema and return its structured drug profile.
    """
    payload = {
        "model": "gpt-4o-2024-08-06",
        "temperature": 0,
        "response_format": LANREOTIDE_SCHEMA,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a regulatory-data assistant. Fill the JSON schema provided via "
                    "response_format exactly. Use only verifiable facts from FDA/Drugs@FDA, "
                    "DailyMed, and EMA labels. If a field cannot be confidently verified, set it to null. "
                    "Market default: US."
                )
            },
            {
                "role": "user",
                "content": f"Return the complete profile for the drug number {drug_number} for the US market."
            }
        ]
    }

    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }

    resp = requests.post(OPENAI_API_URL, json=payload, headers=headers)
    resp.raise_for_status()

    data = resp.json()
    return data["choices"][0]["message"]["content"]


@app.get("/azure-drug-profile")
def get_drug_profile_from_azure(drug_number: str = Query(..., description="Drug identifier like NDC or NDA")):
    """
    Given a drug number, query GPT with the strict JSON schema and return its structured drug profile.
    """
    client = AzureOpenAI(
        api_key=azure_conf["api_key"],
        api_version=azure_conf["api_version"],
        azure_endpoint=azure_conf["endpoint"]
    )
    response = client.chat.completions.create(
        model=azure_conf["deployment_name"],
        temperature=0,
        response_format=LANREOTIDE_SCHEMA,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a regulatory-data assistant. Fill the JSON schema provided via "
                    "response_format exactly. Use only verifiable facts from FDA/Drugs@FDA, "
                    "DailyMed, and EMA labels. If a field cannot be confidently verified, set it to null. "
                    "Market default: US."
                )
            },
            {
                "role": "user",
                "content": f"Return the complete profile for the drug number {drug_number} for the US market."
            }
        ]
    )
    
    return response.choices[0].message["content"]
