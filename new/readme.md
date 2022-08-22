the model was created to run in the browser, 

to run the file in your local browser, use
# flask run 
in this folder, and open the port http://127.0.0.1:5000/  where you will see the web page and can make predictions,
the app was designed to make the minimum value to be 20m2 to ensure prediction integrity 

the original model has been deployed on  https://paris-housing-prediction.herokuapp.com and can be accessed from anywhere on the internet
the app uses mongodb clusters as database where all the data input can be seen, anylysis can still be developed fro the user imput which will help improve the model in the future

the testing of flask app was done using pytest

for security reason, i wont be uploading my password together with the app file, as mongodb rquest your cluster password to be visible, however
the cluster can be changed to your persoal cluster, if you open a free account with  [mongodb](https://account.mongodb.com/account/login)