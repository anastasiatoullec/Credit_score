#Option 1 to start API
cd Credit_score
#docker image build . -t anastasiatoullec/image_credit:latest
#docker login
#docker push anastasiatoullec/image_credit:latest
docker image pull anastasiatoullec/image_credit:latest
docker network create -d bridge net
docker container run -d --rm  --network net -p 8000:8000 --name credit_api_container anastasiatoullec/image_credit:latest

#Option 2 to start API
docker container stop credit_api_container
docker-compose up
