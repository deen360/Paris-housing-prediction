here we automate the workflow, and configure our script to use prefect cloud 

the training of the model is defined using functions and are declared as task, the entry point which is "main" function is where the data we want to use for training is entered.

we can run our prefect locally or on the cloud.  to run prefect on the cloud authication is rquired,
instructions on how to authenticate the keys can be found ![prefect auth](https://docs.prefect.io/ui/cloud-getting-started/)

after we decide where to run prefect, (either locally or on cloud) using the dataset we want as training

docs on from ![prefect deployments](https://docs.prefect.io/tutorials/deploymentss/) was used for this deployment

the following steps are used to deploy  prefect 

#you will be needing 4 terminals(cli) in the same folder to run this in your cli 

have the two servers running in different terminals 

#ensure you have your conda environment and the dependecies installed 

terminal-1 -> you launch the mlflow ui beacuse we are autologging while running the automated training, just to see the parameters, these could be removed if we are only interested in the mse as that will show from he logs displayed 
# mlflow ui
available on http://127.0.0.1:5000


For this project, we use a local Prefect Orion server. Open a separate terminal to inintialize the prefect server we run
terminal -2 -> we lauch the orion server orion
# prefect orion start
which will make prefect avaialble on -> http://127.0.0.1:4200



terminal-3 we run
## prefect deployments build ./paris_flow.py:main -n paris-housing-deployments -t Parisjob
prefect deployments build is the Prefect CLI command that enables you to prepare the settings for a deployments -> this creates a deployment yaml file  in the same folder
     
    
# parameters: {'name':'Paris'}
Open the main-deployments.yaml file and add the parameter 


#these file should be present in the folder 
The flow code in paris_flow.py (mandatory)
The manifest manifest.json (this is not mandatory)
The deployments settings main-deployments.yaml (mandatory)

terminal-3
# prefect deployment apply main-deployment.yaml
Now we use the prefect deployments apply command to create the deployments on the Prefect Orion server, specifying the name of the main-deployments.yaml file.

terminal-3
# prefect deployments ls
To demonstrate that your deployments exists, list all of the current deployments:

terminal-3
#  prefect deployment inspect main/paris-housing-deployments
to display details for a specific deployments.

terminal-3
# prefect agent start -t Parisjob
run the prefect agent start command, passing a -t test option that creates a work queue for test tags. Remember, we configured this same tag "Parisjob" on the deployments at an earlier step, after this, you should already have 3 servers running , the mlflow, the prefect server and the prefect agent

terminal-4
# prefect deployment run main/paris-housing-deployments
the flow will activate and you will see it in the orion ui either on the cloud if its configured or on your local ui 

you can then see the flow in the prefect ui and also the parameters in the mlflow ui, the logs will also display the mse, the shedule can be changed either in the ui or the main-deployments.yaml file.

# NOTE
 if all the steps above seem stressfull, you can equally just turn on the mlfow ui server and the prefect orion server then you run the 
 paris.py as a python script using 
# python paris.py
this will show you almost the same log as the deployment log , note that the paris.py will log an artifact and an mlrun, the paris.py file is the same with paris_flow.py except that it has a main function called below, which make it initialize when run as a python script
