# How to run the  docker container in local

``` bash 
docker run -p 127.0.0.1:8080:8080/tcp taxi_mgmt
```

## Publish a docker container to AWS ECR

```bash
aws configure
aws ecr get-login-password --region us-east-1 | docker login --name AWS --password-stdin 515412545596.dkr.ecr.us-east-1.amazonaws.com
docker build -t 515412545596.dkr.ecr.us-east-1.amazonaws.com/taxicocop-backend:taxi-management-service .
docker images
docker push 515412545596.dkr.ecr.us-east-1.amazonaws.com/taxicocop-backend:taxi-management-service
```

Text from Bob
