# web-service

The model is deployed as a web service using the dockerfile, the 

Ensure terminals(cli) are in the same folder and the environment is activated 

The first thing we do is run the predict.py as a python script using \
** *python predict.py \
when the server is up, we run \
** *python test.py\
in another terminal to be sure both files are configured properly, the test.py terminal should return a prediction of a house price, this shows that both files are configured properly 

so then we build the docker container using the Dockefile in the folder 

to create the envitonmental.yml file, we ran\
** *conda env export --from-history --name project > environmental.yml  \
which helped to get the dependencies that were installed for this project ( the environment name is also named project)

terminal-1 \
** *docker build -t house-price-prediction-service:v1 . \
to build the docker image

terminal-1 \
** *gunicorn --bind=0.0.0.0:9696 predict:app \
to listen to the port we use gunicorn, while the server  is up 

terminal-2 \
** *python test.py \
we run the test.py in another terminal, when it returns a prediction, that means our container is working properly as a web-service 

we deploy the model to the web in 06-flask-deployment
