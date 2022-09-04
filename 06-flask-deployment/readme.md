#flask-deployment

the model was created to run in the browser, 

to run the file in your local browser, use \
** *flask run 
in this folder, and open the port http://127.0.0.1:5000/  ,where you will see the web page and can make predictions based on squaremeters input,
the app was designed to make the minimum value to be 20m2 to ensure prediction integrity 

The original model has been deployed on  https://paris-housing-prediction.herokuapp.com and can be accessed from anywhere on the internet. \
the app uses mongodb clusters as database where all the data input can be seen, anylysis can still be developed from the user imput which will help to improve the model in the future


The testing of flask app was done using pytest\ 
to run the test we use    pytest test/


model available on internet [paris-prediction](https://paris-housing-prediction.herokuapp.com/predict/)
