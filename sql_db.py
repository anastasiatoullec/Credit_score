#pip install sqlalchemy

import sqlite3, sqlalchemy
from sqlalchemy import Table, Column, Integer, String, ForeignKey, MetaData, create_engine, text, inspect, Float
import joblib

engine = create_engine("sqlite:///credit_customer.db")

meta = MetaData()

customer= Table(
    'customer', meta, 
    Column('ID', String, primary_key=True), 
    Column('Customer_ID', String), 
    Column('Name', String),
    Column('Age', Integer), 
    Column('SSN', String), 
    Column('Occupation', String), 
    Column('Annual_Income', Float),
    Column('Monthly_Inhand_Salary', Float)        
)

credit= Table(
    'credit', meta, 
    Column('ID_Credit', Integer, primary_key=True),
    Column('ID', String, ForeignKey("customer.ID")), 
    Column('Num_Bank_Accounts', Integer),
    Column('Interest_Rate', Integer),
    Column('Num_of_Loan', Integer), 
    Column('Type_of_Loan', String),
    Column('Delay_from_due_date', Integer), 
    Column('Num_of_Delayed_Payment', Integer), 
    Column('Changed_Credit_Limit', Float),
    Column('Num_Credit_Inquiries', Float),
    Column('Credit_Mix', String),
    Column('Outstanding_Debt', Float),
    Column('Credit_Utilization_Ratio', Float), 
    Column('Payment_of_Min_Amount', String),
    Column('Total_EMI_per_month', Float),
    Column('Amount_invested_monthly', Float), 
    Column('Payment_Behaviour', String),
    Column('Monthly_Balance', Float),
    Column('Credit_History_Age_Years', Integer),
    Column('Credit_History_Age_Months', Integer)    
)

meta.create_all(engine)

df_customer = joblib.load('./df_customer.pkl')#file with clean data
values = list(zip(*map(df_customer.get, df_customer)))


with engine.connect() as connection:
    with connection.begin() as transaction:
        try:
            # We indicate the format of a tuple of this table
            markers = ','.join('?' * len(values[0])) 
            # We use the SQL language in text format where markers is the format of a tuple
            ins = 'INSERT INTO {tablename} VALUES ({markers})'
            # This particular format is specified using the format member function
            ins = ins.format(tablename=customer.name, markers=markers)
            # Finally we can use the tuples created by executing the SQL command
            connection.execute(ins, values)
        except:
            transaction.rollback()
            raise
        else:
            transaction.commit()

df_credit = joblib.load('./df_credit.pkl')#file with clean data
values_credit = list(zip(*map(df_credit.get, df_credit)))

with engine.connect() as connection:
    with connection.begin() as transaction:
        try:
            # We indicate the format of a tuple of this table
            markers = ','.join('?' * len(values_credit[0])) 
            # We use the SQL language in text format where markers is the format of a tuple
            ins = 'INSERT INTO {tablename} VALUES ({markers})'
            # This particular format is specified using the format member function
            ins = ins.format(tablename=credit.name, markers=markers)
            # Finally we can use the tuples created by executing the SQL command
            connection.execute(ins, values_credit)
        except:
            transaction.rollback()
            raise
        else:
            transaction.commit()

conn = engine.connect()