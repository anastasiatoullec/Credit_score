import pandas as pd
import joblib

df = pd.read_csv(filepath_or_buffer = 'test.csv',
                           sep = ',',
                           header = 0)

#Change missing Names to MrX
#df['Name'] = df['Name'].fillna('MrX')
df=df.dropna(subset=['Name'])
#Replace "_", "", then transform data into integer and chose age between 0 -110 years old
df["Age"] = df["Age"].apply(lambda x: x.replace("_", ""))
df["Age"] = df["Age"].astype(int)
df = df[(df['Age'] > 0) & (df['Age']<110)]

#Eliminate not normal values like '#F%$D@*&8'..
df=df.loc[df["SSN"].str.match("[0-9][0-9][0-9]\-[0-9][0-9]\-[0-9][0-9][0-9][0-9]")]

#Escape missing jobs
df = df[df["Occupation"] != "_______"]

#Replace "_", "", then transform data into float
df['Annual_Income'] = df['Annual_Income'].apply(lambda x: x.replace("_", ""))
df["Annual_Income"] = df["Annual_Income"].astype(float)

#Fulfill missing values with median values of column 'Monthly_Inhand_Salary'
df['Monthly_Inhand_Salary'] = df['Monthly_Inhand_Salary'].fillna(df['Monthly_Inhand_Salary'].median())

#Replace "_" and choosing only positive values then to integers
df['Num_of_Loan'] = df['Num_of_Loan'].apply(lambda x: x.replace("_", ""))
df['Num_of_Loan'] = df['Num_of_Loan'].apply(lambda x: x.replace("-", ""))
df['Num_of_Loan'] = df["Annual_Income"].astype(int)

#Fulfill missing values with mode values of column 'Type_of_Loan'
df['Type_of_Loan'] = df['Type_of_Loan'].fillna(df['Type_of_Loan'].mode()[0])

#Choosing only positive values for Delay_from_due_date
df = df[df['Delay_from_due_date'] > 0]

#Delete lines with missing values, replace "_" and choosing only positive values -> integers
df = df.dropna(axis = 0, how = 'all',subset=['Num_of_Delayed_Payment'])
df['Num_of_Delayed_Payment'] = df['Num_of_Delayed_Payment'].apply(lambda x: x.replace("_", ""))
df['Num_of_Delayed_Payment'] = df['Num_of_Delayed_Payment'].apply(lambda x: x.replace("-", ""))
df['Num_of_Delayed_Payment'] = df['Num_of_Delayed_Payment'].astype(int)

#Zeros transformation to be able to make float after
df['Changed_Credit_Limit'] = df['Changed_Credit_Limit'].apply(lambda x: x.replace("_", "0"))#could not convert string to float: ''
df['Changed_Credit_Limit'] = df['Changed_Credit_Limit'].astype(float)

#Fulfill missing values with meadian values of column Num_Credit_Inquiries'
df['Num_Credit_Inquiries'] = df['Num_Credit_Inquiries'].fillna(df['Num_Credit_Inquiries'].median())

#Replace "_" with neutral value
df['Credit_Mix'] = df['Credit_Mix'].apply(lambda x: x.replace("_", "Standard"))

#Replace "_" anf float transformation
df['Outstanding_Debt'] = df['Outstanding_Debt'].apply(lambda x: x.replace("_", ""))
df['Outstanding_Debt'] = df['Outstanding_Debt'].astype(float)


#'Credit_History_Age' transformation into suitable values, fulfill first missing values
#exemple: '22 Years and 9 Months' --> ['Credit_History_Age_Years']= 22 and ['Credit_History_Age_Months']= 9
df['Credit_History_Age'] = df['Credit_History_Age'].fillna(df['Credit_History_Age'].mode()[0]) 
df['Credit_History_Age_Years'] = df['Credit_History_Age'].apply(lambda date: date.split(' ')[0])
df['Credit_History_Age_Months'] = df['Credit_History_Age'].apply(lambda date: date.split(' ')[3])
df['Credit_History_Age_Months'] = df['Credit_History_Age_Months'].astype(int)
df['Credit_History_Age_Years'] = df['Credit_History_Age_Years'].astype(int)
df=df.drop(['Credit_History_Age'], axis=1)

#Replace mistakes in worlds No
df['Payment_of_Min_Amount'] = df['Payment_of_Min_Amount'].apply(lambda x: x.replace('NM', 'No'))

#Fulfill missing values, clean "_" and transforme to Float
df['Amount_invested_monthly'] = df['Amount_invested_monthly'].fillna(df['Amount_invested_monthly'].mode()[0]) #to save values need to use mode not mean, before transformation float
df['Amount_invested_monthly'] = df['Amount_invested_monthly'].apply(lambda x: x.replace("_", ""))
df['Amount_invested_monthly'] = df['Amount_invested_monthly'].astype(float) #nok trasforme '236.64268203272135' -> 236.64268203272135

#Remplace anormal values'!@9#%8' 
df['Payment_Behaviour'] = df['Payment_Behaviour'].apply(lambda x: x.replace('!@9#%8', df['Payment_Behaviour'].mode()[0]))

#Fulfill missing values, clean "_" and transforme to Float
df['Monthly_Balance'] = df['Monthly_Balance'].fillna(df['Monthly_Balance'].mode()[0]) #to save values need to use mode not mean, before transformation float
df['Monthly_Balance'] = df['Monthly_Balance'].apply(lambda x: x.replace("_", ""))
df['Monthly_Balance'] = df['Monthly_Balance'].astype(float)  #nok trasforme '236.64268203272135' -> 236.64268203272135


#print(df)
#Create a primary key for future credit table
#df['ID_Credit']= [i for i in range(38971)]
df['ID_Credit']= [i for i in range(35023)]


#df_customer = df[['Customer_ID', 'Name','SSN','Occupation','Annual_Income','Monthly_Inhand_Salary']]
df_customer = df[['Customer_ID', 'Name','SSN','Occupation']]
df_customer = df_customer.drop_duplicates()
df_income = df[['ID', 'Customer_ID','Annual_Income','Monthly_Inhand_Salary','Month']]
df_credit = df[['ID_Credit','ID','Num_Bank_Accounts', 'Interest_Rate','Num_of_Loan','Type_of_Loan','Delay_from_due_date','Num_of_Delayed_Payment',
'Changed_Credit_Limit', 'Num_Credit_Inquiries', 'Credit_Mix', 'Outstanding_Debt', 'Credit_Utilization_Ratio', 'Payment_of_Min_Amount',
'Total_EMI_per_month', 'Amount_invested_monthly', 'Payment_Behaviour', 'Monthly_Balance', 'Credit_History_Age_Years','Credit_History_Age_Months']]

print(df_credit.head(10))

joblib.dump(df_customer, './df_customer.pkl')
joblib.dump(df_credit, './df_credit.pkl')
joblib.dump(df_income,'./df_income.pkl')
