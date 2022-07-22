#pip3 install fastapi uvicorn
#pip install passlib[bcrypt]
#uvicorn Credit_api:api --reload
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
    num_of_loan:int
    type_of_loan:str
    delay_from_due_date: int
    num_of_delayed_payment: int
    changed_credit_limit: float
    num_credit_inquiries: float
    credit_mix: str
    outstanding_debt: float
    credit_utilization_ratio: float
    payment_of_min_amount: str
    total_emi_per_month: float
    amount_invested_monthly: float
    payment_behaviour: str
    monthly_balance: float
    credit_history_age_years: int
    credit_history_age_months: int

class Income(BaseModel):
    income_id:str
    customer_id: str
    annual_income: int
    monthly_salary: int
    month: str

api = FastAPI(
    title="Credit score classification API",
    description="Over the years, the global finance company has collected basic bank details and gathered a lot of credit-related information."
     "This Api represents an intelligent system to segregate the people into credit score brackets to reduce the manual efforts."
     "API allows to request database of the global finance company.",
    version="1.0.0")
    
@api.get("/welcome", tags=['Welcome'])
def welcome():
    """Welcome to our page, we are glad to see you!
    """
    return {'Hello, Bonjour, Hola, Zdravstvuyte, Nǐn hǎo, Salve, Konnichiwa, Guten Tag, Olá, Anyoung haseyo, Asalaam alaikum, Goddag'}


@api.get('/customers',tags=['General credit information'])
async def get_customers(): 
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

@api.get('/incomes',tags=['General credit information'])
async def get_incomes(): 
    with engine.connect() as connection:
        results = connection.execute('SELECT * FROM income limit 10;')

        results = [
        Income(
            income_id=i[0],
            customer_id=i[1],
            annual_income=i[2],
            monthly_salary=i[3],
            month=i[4]
           
            ) for i in results.fetchall()]

    return results
        
@api.get('/credits',tags=['General credit information'])
async def get_credits(): 
    with engine.connect() as connection:
        results = connection.execute('SELECT * FROM credit limit 10;')


        results = [
        Credit(
            credit_id=i[0],
            customer_id=i[1],
            num_bank_account=i[2],
            interest_rate=i[3],
            num_of_loan=i[4],
            type_of_loan=i[5],
            delay_from_due_date=i[6],
            num_of_delayed_payment=i[7],
            changed_credit_limit=i[8],
            num_credit_inquiries=i[9],
            credit_mix=i[10],
            outstanding_debt=i[11],
            credit_utilization_ratio=i[12],
            payment_of_min_amount=i[13],
            total_emi_per_month=i[14],
            amount_invested_monthly=i[15],
            payment_behaviour=i[16],
            monthly_balance=i[17],
            credit_history_age_years=i[18],
            credit_history_age_months=i[19]
                        
            ) for i in results.fetchall()]

    return results  

@api.post("/fill_customer",tags=['New Customer'])
def fill_Customer(cust:Customer):
    """
    Here we can add a information for a new customer
    """
    features = [[
    cust.customer_id,
    cust.name,
    cust.ssn,
    cust.occupation
    ]]
    #function to send a new information
    return {
        "New customer":features
    }

@api.post("/fill_income",tags=['New Customer'])
def fill_Income(inc:Income):
    """
    Here we can add a information of income for a new customer
    """
    features = [[
    inc.income_id,
    inc.customer_id,
    inc.annual_income,
    inc.monthly_salary,
    inc.month
    ]]
    #function to send a new information
    return {
        "New income for a customer":features
    }

@api.post("/fill_credit",tags=['New Customer'])
def fill_Credit(crd:Credit):
    """
    Here we can add a credit information for a new customer
    """
    features = [[
    crd.credit_id,
    crd.customer_id,
    crd.num_bank_account,
    crd.interest_rate,
    crd.num_of_loan,
    crd.type_of_loan,
    crd.delay_from_due_date,
    crd.num_of_delayed_payment,
    crd.changed_credit_limit,
    crd.num_credit_inquiries,
    crd.credit_mix,
    crd.outstanding_debt,
    crd.credit_utilization_ratio,
    crd.payment_of_min_amount,
    crd.total_emi_per_month,
    crd.amount_invested_monthly,
    crd.payment_behaviour,
    crd.monthly_balance,
    crd.credit_history_age_years,
    crd.credit_history_age_months
    ]]
    #function to send a new information
    return {
        "New credit information":features
    }



@api.get('/max_income_occupation',tags=['Requests'])
async def max_income_occupation():
    """
    Find customers with maximum annual income and show their occupation
    """
    connection = sqlite3.connect('credit_customer.db')
    cursor = connection.cursor()
    sqlite_select_query = """
    SELECT occupation, Max(annual_income) as MaxIncome 
    FROM customer INNER JOIN income ON customer.customer_id = income.customer_id  
    GROUP BY occupation ORDER BY MaxIncome DESC LIMIT 10"""
   #sqlite_select_query = """SELECT occupation, Max(annual_income) as MaxIncome FROM(customer INNER JOIN income ON customer.customer_id = income.customer_id ) GROUP BY occupation ORDER BY MaxIncome DESC LIMIT 10"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()

    return {"Occupation and Annual income in euros" : records }

@api.get('/min_income_occupation',tags=['Requests'])
async def min_income_occupation():
    """
    Find customers with minimum annual income and show their occupation
    """
    connection = sqlite3.connect('credit_customer.db')
    cursor = connection.cursor()
    sqlite_select_query = """
    SELECT occupation, Min(annual_income) as MinIncome 
    FROM customer INNER JOIN income ON customer.customer_id = income.customer_id  
    GROUP BY occupation ORDER BY MinIncome DESC LIMIT 10"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()

    return {"Occupation and Annual income in euros" : records }

@api.get('/avg_income_occupation',tags=['Requests'])
async def avg_income_occupation():
    """
    Find customers with average annual income and show their occupation
    """
    connection = sqlite3.connect('credit_customer.db')
    cursor = connection.cursor()
    sqlite_select_query = """
    SELECT occupation, AVG(annual_income) as AVGIncome 
    FROM customer INNER JOIN income ON customer.customer_id = income.customer_id  
    GROUP BY occupation ORDER BY AVGIncome DESC LIMIT 10"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()

    return {"Occupation and Annual income in euros" : records }

@api.get('/occupations',tags=['Requests'])
async def occupations():
    """
    Show all occupations 
    """
    connection = sqlite3.connect('credit_customer.db')
    cursor = connection.cursor()
    sqlite_select_query = """SELECT Occupation, COUNT(*) FROM customer GROUP BY Occupation"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()

    return records

@api.get('/type_of_loan_Scientist',tags=['Requests'])
async def type_of_loan_Scientist():
    """
    Find occupations by type of loan 
    """
    connection = sqlite3.connect('credit_customer.db')
    cursor = connection.cursor()
    sqlite_select_query = """
    SELECT Type_of_Loan, COUNT(*)
    FROM customer INNER JOIN credit ON customer.customer_id = credit.customer_id  
    WHERE Occupation='Scientist'  GROUP BY Occupation LIMIT 20"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()

    return {"The most frequent type of loan for scientists" : records }
