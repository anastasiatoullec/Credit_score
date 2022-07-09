#pip3 install fastapi uvicorn
#pip install passlib[bcrypt]
#uvicorn credit_api:api --reload
#http://127.0.0.1:8000/docs ou http://localhost:8000/docs

import uvicorn, requests
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import json

api = FastAPI(
    title="Credit score classification API",
    description="Over the years, the global finance company has collected basic bank details and gathered a lot of credit-related information."
     "This Api represents an intelligent system to segregate the people into credit score brackets to reduce the manual efforts."
     "API allows to request database of the global finance company.",
    version="1.0.0", openapi_tags=[
        {
        'name': 'Welcome',
        'description': 'This function returns greetings'
    },
    {   'name': 'First test request' },
])


@api.get("/welcome", tags=['Welcome'])
def welcome():
    """Welcome to our page, we are glad to see you!
    """
    return {'Hello, Bonjour, Hola, Zdravstvuyte, Nǐn hǎo, Salve, Konnichiwa, Guten Tag, Olá, Anyoung haseyo, Asalaam alaikum, Goddag'}

@api.get("/first", tags=['First test request'])
def first_function():
    """This function returns 2 lines of our model!
    """
    df = joblib.load('./df.pkl')#file with clean data
    test_df = df.head(2)
    return {
        "Credit score dataframe":test_df.to_json(orient='records')
    }
