cd Credit_score
#docker image build . -t anastasiatoullec/image_credit:latest
#docker push anastasiatoullec/image_credit:latest
docker image pull anastasiatoullec/image_credit:latest
docker network create -d bridge net
#docker container run -d --rm  --network net -p 8000:8000 --name credit_api_container anastasiatoullec/image_credit:latest
cd

cd Credit_score
#docker container stop credit_api_container
docker-compose up
