here we focus on the monitoring of our process, to see if we have a data drift
the monitoring here will be done both in online and in batch model, using evidently, mongo db, primethus and grafana 

->for the online monitoring
first we run the command (in the terminal)
# python prepare.py 
which downloads 2 files from the s3 bucket -> ParisHousing_period_01.parquet which is used as the reference file and ParisHousing_period_04.parquet which is used as new data sent

# docker compose up  --build 
we run docker compose up to start the container, this build the docker container 

this starts all the files applications required, starting from evidently, mongodb, prometheus and grafana

# python send_data.py
with the command above we send data to the docker container running using "python send_data.py", . the [send_data.py](mlops-project/05-monitoring/send_data.py) sends the squaremters in the file ParisHousing_period_04.parquet to the to the container each second, and it receives a response of the predicted result, this result is will be automatically logged into our mongodb database, wghich is available on ![pymongo_database(online)](mlops-project/05-monitoring/pymongo_database(online).ipynb).

# jupyter-notebook
to see the data logged, we open the pymongo_database(online).ipynb file to see the data logging in our pymongo collection
-
->image
# http://localhost:3000                 username: admin     password: admin
while the data is sending, we open the grafana ui 
    go to dashboards
        go to "evidently data drift dashboard" and you will see the data drift there for the "squaremeters" and "category(luxury or basic)"
-->image
# http://localhost:9091/ 
we can also chek the prometheus ui to see the data and run some promql queries 

# evidently:data_drift:p_value
to run some promql queries we can input the above line in the search bar and we see the drift p values, we can also check the graph too in the prometheus ui, or search "up" to see the instances running, 0 means machine is down nd 1 means machine is up


#for the batch monitoring
here we make use of the prefect_batch.py file