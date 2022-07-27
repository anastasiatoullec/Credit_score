FROM debian:latest
COPY ./requirements.txt .
RUN apt-get update && apt-get install python3-pip -y
RUN pip install -r requirements.txt
COPY credit_customer.db /./credit_customer.db
COPY Credit_api.py /./Credit_api.py
WORKDIR /.
EXPOSE 8000
CMD uvicorn Credit_api:api --host 0.0.0.0