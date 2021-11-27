# API creation with python
example prokect how to create API work with flas and python

#########How this Application works############

We have created python rest API with flask library which will run inside the docker container.

Once the Application will start then we can see the data by hitting the below url.
 http://<IP>:port/info


Pre-requisite:-

1) Docker should be installed on the server.

Build Docker image:-

We have a requirement.txt in which we have menioned all the dependency which will required to run the application.

we have a Dockerfile in which we have installing dependency, copying all the required folders and running the application.

Command to create the docker image.

docker build -t api:1.0 .

Run the docker image:-

docker run -d -p <port>:5000 -e port=<port> -e loglevel=<loglevel> --name API app:1.0


