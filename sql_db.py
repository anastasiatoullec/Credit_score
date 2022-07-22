#pip install sqlalchemy

import sqlite3, sqlalchemy
from sqlalchemy import Table, Column, Integer, String, ForeignKey, MetaData, create_engine, text, inspect, Float
import joblib

engine = create_engine("sqlite:///credit_customer.db",connect_args={"check_same_thread": False})

sql1 = text('DROP TABLE IF EXISTS customer;')
result = engine.execute(sql1)
sql2 = text('DROP TABLE IF EXISTS income;')
result = engine.execute(sql2)
sql3 = text('DROP TABLE IF EXISTS credit;')
result = engine.execute(sql3)

meta = MetaData()

customer= Table(
    'customer', meta,  
    Column('Customer_ID', String, primary_key=True), 
    Column('Name', String),
    Column('SSN', String), 
    Column('Occupation', String),     
)

income= Table(
    'income', meta,  
    Column('ID', String, primary_key=True), 
    Column('Customer_ID', String, ForeignKey("customer.Customer_ID")), 
    Column('Annual_Income', Float),
    Column('Monthly_Inhand_Salary', Float) , 
    Column('Month', String)      
)


credit= Table(
    'credit', meta, 
    Column('ID_Credit', Integer, primary_key=True),
    Column('Customer_ID', String, ForeignKey("customer.Customer_ID")), 
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

def insert_data(values, table_name):
    with engine.connect() as connection:
        with connection.begin() as transaction:
            try:
                # We indicate the format of a tuple of this table
                markers = ','.join('?' * len(values[0])) 
                # We use the SQL language in text format where markers is the format of a tuple
                ins = 'INSERT INTO {tablename} VALUES ({markers})'
                # This particular format is specified using the format member function
                ins = ins.format(tablename=table_name, markers=markers)
                # Finally we can use the tuples created by executing the SQL command
                connection.execute(ins, values)
            except:
                transaction.rollback()
                raise
            else:
                transaction.commit()

df_customer = joblib.load('./df_customer.pkl')#file with clean data
values = list(zip(*map(df_customer.get, df_customer)))
insert_data(values, customer.name)


df_credit = joblib.load('./df_credit.pkl')#file with clean data
values_credit = list(zip(*map(df_credit.get, df_credit)))
insert_data(values_credit, credit.name)

df_income = joblib.load('./df_income.pkl')#file with clean data
values_income = list(zip(*map(df_income.get, df_income)))
insert_data(values_income, income.name)



