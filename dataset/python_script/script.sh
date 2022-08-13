
#here you put your personal kaggle keys on your kaggle account 
export KAGGLE_USERNAME=yusufkamorudeen
export KAGGLE_KEY=f5779e2007b3e41b613275a975fd5a7c



DATASET_ID=mssmartypants
DATASET_NAME=paris-housing-classification

kaggle datasets download -d $DATASET_ID/$DATASET_NAME --unzip

echo "Download from kaggle $DATASET_ID/$DATASET_NAME is succesful "


#we create a folder where we will put the data when we split it 
mkdir data