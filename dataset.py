import sqlite3, sqlalchemy
from sqlalchemy import Table, Column, Integer, String, ForeignKey, MetaData, create_engine, text, inspect, Float
import joblib


engine = create_engine("sqlite:///credit.db")
meta = MetaData()
credit= Table(
    'credit', meta, 
    Column('ID', String, primary_key=True), #chiffres+tirets==String?
    Column('Customer_ID', String), 
    Column('Month', String),
    Column('Name', String),
    Column('Age', Float), #Integer?
    Column('SSN', String),
    Column('Occupation', String), 
    Column('Annual_Income', Float),
    Column('Monthly_Inhand_Salary', Float), 
    Column('Num_Bank_Accounts', Integer),
    Column('Num_Credit_Card', Integer), 
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
    Column('Credit_History_Age', String),
    Column('Payment_of_Min_Amount', String),
    Column('Total_EMI_per_month', Float),
    Column('Amount_invested_monthly', Float), 
    Column('Payment_Behaviour', String),
    Column('Monthly_Balance', Float)
    
)
meta.create_all(engine)

values = joblib.load('./data.pkl')#file with data cleaning

with engine.connect() as connection:
    with connection.begin() as transaction:
        try:
            # We indicate the format of a tuple of this table
            markers = ','.join('?' * len(values[0])) 
            # We use the SQL language in text format where markers is the format of a tuple
            ins = 'INSERT INTO {tablename} VALUES ({markers})'
            # This particular format is specified using the format member function
            ins = ins.format(tablename=credit.name, markers=markers)
            # Finally we can use the tuples created by executing the SQL command
            connection.execute(ins, values)
        except:
            transaction.rollback()
            raise
        else:
            transaction.commit()


conn = engine.connect() #Instantiate the Connection class in a variable named conn
