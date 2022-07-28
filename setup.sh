cd Credit_score
#cd db
#docker image build . -t anastasiatoullec/image_db:latest
#docker push anastasiatoullec/image_db:latest
#cd ..
#cd api_credit
#docker image build . -t anastasiatoullec/image_api_credit:latest
#docker push anastasiatoullec/image_api_credit:latest
#cd ..
#Create a new network
docker network create -d bridge net
#Download images of api and batabase
docker image pull anastasiatoullec/image_api_credit:latest
docker image pull anastasiatoullec/image_api_credit:latest
#Start docker containers
docker-compose up
