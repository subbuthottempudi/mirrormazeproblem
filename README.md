# mirrormazeproblem

docker build . -t sparkhome

docker exec -it --user root sparkhome /bin/bash

docker pull jupyter/pyspark-notebook:python-3.10.10

---------------------------------------------
docker build . -t sparkhome
docker image ls
docker run -p 8888:8888 --name spark -d sparkhome