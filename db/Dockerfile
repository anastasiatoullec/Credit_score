FROM debian:latest
COPY ./requirements.txt .
RUN apt-get update && apt-get install python3-pip -y
RUN pip install -r requirements.txt
COPY test.csv /./test.csv
COPY cleaning.py /./cleaning.py
COPY df_credit.pkl /./df_credit.pkl
COPY df_customer.pkl /./df_customer.pkl
COPY df_income.pkl /./df_income.pkl
COPY sql_db.py /./sql_db.py
COPY credit_customer.db /./credit_customer.db
WORKDIR /.
EXPOSE 8001
RUN python3 /./cleaning.py
CMD python3 /./sql_db.py
