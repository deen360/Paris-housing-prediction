
#this script is already embeded in the python script and it will be executed automatically when the pytho script is executed

#here you put your personal kaggle keys from your kaggle account 
export KAGGLE_USERNAME=yusufkaxxxxxxxxxxxxx
export KAGGLE_KEY=f5779e2007b3e41b613xxxxxxxxxxxx


DATASET_ID=mssmartypants
DATASET_NAME=paris-housing-classification

kaggle datasets download -d $DATASET_ID/$DATASET_NAME --unzip




#we create a folder where we will put the data when we split it 
mkdir data