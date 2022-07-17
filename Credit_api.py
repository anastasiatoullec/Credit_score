#pip3 install fastapi uvicorn
#pip install passlib[bcrypt]
#uvicorn credit_api:api --reload
#http://127.0.0.1:8000/docs ou http://localhost:8000/docs

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
#import joblib
#import pandas as pd
import json
from sqlalchemy import  create_engine
import  sqlite3


database_name = 'credit_customer.db'


# recreating the URL connection
connection_url = 'sqlite:///{database}'.format(database=database_name)

engine = create_engine(connection_url)

class Customer(BaseModel):
    customer_id: str
    name: str 
    ssn: str 
    occupation: str

class Credit(BaseModel):
    credit_id: int
    customer_id: str 
    num_bank_account: int 
    interest_rate:int

class Income(BaseModel):
    income_id:str
    customer_id: str
    annual_income: int
    monthly__salary: int
    month: str

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


@api.get('/customers')
async def get_users(): 
    with engine.connect() as connection:
        results = connection.execute('SELECT * FROM customer limit 10;')

        results = [
        Customer(
            customer_id=i[0],
            name=i[1],
            ssn=i[2],
            occupation=i[3]
            ) for i in results.fetchall()]

    return results

@api.get('/incomes')
async def get_users(): 
    with engine.connect() as connection:
        results = connection.execute('SELECT * FROM income limit 10;')

        results = [
        Income(
            income_id=i[0],
            customer_id=i[1],
            annual_income=i[2],
            monthly__salary=i[3],
            month=i[4]
           
            ) for i in results.fetchall()]

    return results
        
@api.get('/credits')
async def get_users(): 
    with engine.connect() as connection:
        results = connection.execute('SELECT * FROM credit limit 10;')


        results = [
        Credit(
            credit_id=i[0],
            customer_id=i[1],
            num_bank_account=i[2],
            interest_rate=i[3]
         
            #autres champs à ajouter
            
            ) for i in results.fetchall()]

    return results  
    


@api.get("/welcome", tags=['Welcome'])
def welcome():
    """Welcome to our page, we are glad to see you!
    """
    return {'Hello, Bonjour, Hola, Zdravstvuyte, Nǐn hǎo, Salve, Konnichiwa, Guten Tag, Olá, Anyoung haseyo, Asalaam alaikum, Goddag'}

'''
@api.get("/first", tags=['First test request'])
def first_function():
    """This function returns 2 lines of our model!
    """
    df = joblib.load('./df.pkl')#file with clean data
    test_df = df.head(2)
    return {
        "Credit score dataframe":test_df.to_json(orient='records')
    }
'''
