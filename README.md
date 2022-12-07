# docker_iris_clf
simple iris clf docker image

test flask app by filling in the form and click 'run' or by entering this into browser
http://localhost:5001/score?petal_length=5.0&petal_width=2.0&sepal_length=3.5&sepal_width=1.0

pip freeze > requirements.txt

docker build . -t <image_name>

docker run -d -p 5001:5001 <image_name>

test container by entering this into browser
http://localhost:5001/score?petal_length=5.0&petal_width=2.0&sepal_length=3.5&sepal_width=1.0



### loading image to dockerhub
docker login -u <your_docker_id> --password <your_docker_password>

docker build -t <your_docker_id>/<image_name>:<image_version>

docker push <your_docker_id>/<image_name>

#### see image at 
hub.docker.com/repository/docker/<your_docker_id>/<image_name>

#### pull image 
docker pull <your_docker_id>/<image_name>:<image_version>

