![img](credit-card.png)
# Topics:
### - Credit Card Fraud Detection with simple ML models &emsp;[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Luciferxx/Credit_Card_Fraud_Detection/blob/master/Credit%20Card%20Fraud%20Detection%20(Simple%20ML).ipynb)
 - Loading Credit Card Transaction data
 - Data analysis:
     - Handling NULL values
     - Correlation of Columns
     - Data Scalling and Normalization
     - Class Distribution Skewness
 - Model Building
     - Grid Search
     - K-Fold
     - Cross Validation 
     - Models
        - Logistic Regression
        - K-Nearest Neighbors
        - Support Vestor Classifier
        - Decision Tree Classifier
     - Learning Curves (Training Curves)
     - ROC (Receiver Operating Characteristic)
        
### - Credit Card Fraud Detection using Deep Learning Techniques &emsp; [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Luciferxx/Credit_Card_Fraud_Detection/blob/master/Credit%20Card%20Fraud%20Detection%20(Neural%20Networks).ipynb)
  - Loading Credit Card Transaction data
  - Data analysis:
      - Handling NULL values
      - Correlation of Columns
      - Data Scalling and Normalization
      - Class Distribution Skewness
  - Splitting data
  - Model
      - 2 layered Neural Network
      - Training Curve
      - Validation Curve
      - Saving trained Model for deployment
      
### - Deployment
  - Docker Installation
  - Install TF Serving Image from Docker Hub
  - Local Deployment of trained model 
  - Remote Deployment on Heroku
  - Creating a REST API to use deployed model to create a Web Application
  
# Deployment:
Docker is a reliable tool used for deployment. Tensorflow Serving Image is used to deploy trained models locally as well as to cloud platforms such as AWS, Google Cloud, Heroku etc using Docker containers.

## Install Docker: 
- For [Windows](https://docs.docker.com/docker-for-windows/install/)
- For [MacOS](https://docs.docker.com/docker-for-mac/install/)
- For [Linux](https://docs.docker.com/engine/install/)

## Download Tensorflow Serving Image locally:
- Open your terminal or command prompt in which docker is installed
 
  `docker pull tensorflow/serving`

## Download the trained model:
- After running the 2nd Colab notebook, you will download the trained model
- The model structure will be of the form:
    
      saved_model
          |___ 1
               |___ variables
               |       |___ variables.data-00000-of-00001
               |       |___ variables.index
               |
               |___ saved_model.pb

## Time for deployment

- Note: Whatever is the current version for your saved_model Tensorflow serving will detect that and deploy

- Open the terminal again.

- Copy the directory path to the respective saved model file 

`docker run -it --rm -p 8500:8500 -p 8501:8501 -v "Copied_path_to_the_saved_model:/models/name_of_model/" -e MODEL_NAME=name_of_model tensorflow/serving`
- `docker run` command is to run the container
- `-it`is used in order to allocate a tty for the container process.
- `-rm` deletes the container once it has been stopped although doesn't removes the image
- `-p`is used to define the port number 
- `8500` is used to query using gRPC 
- `8501` is used to query using REST API
- `-v` Volume mount
- Copied_path_to_the_saved_model Eg: /mnt/d/saved_model 
- `/models/saved_model` means that there is a folder in the container from which Tensorflow serving loads the model for deployment. 
- This models folder exist inside that container
- Note: saved_model is the name of your saved_model which needs to be same as the one you have saved with.
- In this case  it was saved_model
- `-e` environment variable
- `MODEL_NAME` as the name suggests it should be the same as the name you have defined
- `tensorflow/serving` is the mandatory to right because by this you are declaring of what image you want to create container of.

- In case, if you want to provide a name to your container. It can be done by using the --name tag

- For eg: `docker run --name "Model_Container" #Rest of the command--> `

## How do we query the docker deployment

# REST API query
- Refer to the cell in Fraud_Detection.ipynb to see the implementation
- X_Test is your test data on which you want to conduct tests on
```
import json
a = np.array(X_test) 
input_data_json = json.dumps({
    "signature_name":"serving_default",
    "instances":a.tolist()
})

import requests
SERVER_URL = "http://localhost:8501/v1/models/saved_model:predict"
Note: Again replace your saved model name with saved_model. Rest all remains some
response = requests.post(SERVER_URL,data=input_data_json)
response.raise_for_status()
response = response.json()
y_prob = np.array(response["predictions"])
```

- Well this is one of the way to approach creating the local host server on docker

# SECTION 2

- From following the steps below, you can deploy on local host as well as remote cloud server
- Other is using the dockerfile for deployment 

- Create  any folder inside that create a models folder. Inside the models folder, keep your saved_model folder.
- Now you can clone the dockerfile from the github repository.

- Keep this dockerfile with models folder

- Open your Dockerfile using terminal or Notepad
- Note: This dockerfile doesn't has any  extension

- Change the `MODEL_NAME`  variable and change the name of your model below as well.
`COPY models/chat_model models/chat_model` 

- This command will help you to store your model into the tensorflow serving container

- Now , lets go inside the folder where we have the docker file using the terminal
- Note: folder_name is the name of the folder which consists your docker file and the model files

- Run the following command: `docker build -t <folder_name> . `

- Note: the period at the end of the command and the folder_name should be in lower case
- This command will compile your dockerfile and makes sure everything will run fine.

- Last But not the least: Run the following command: `docker run -p 8501:8501 -e PORT=8501 -t <folder_name>`
- `-t` stands for the tag or the name of the container 

- This commands sets up your local server on your laptop to run your tensorflow model.

## Refer to the REST API query section in the section 1.

## HEROKU DEPLOYEMENT:-

- First, create an account on Heroku. If you already have one, skip to the next step.

- Install Heroku CLI 

- open your respective terminal where you installed the Heroku CLI

- Lets check heroku version if everything is perfectly installed:
- Command: `heroku version`

- Next login to the Heroku CLI:
`heroku container:login`
- This command will redirect you to your default browser where you have to login.

- Next, Lets create an app on Heroku using the following command:

- `Heroku create <the name of the container which is available on the heroku service>` eg . Chatbot

- `Heroku container:push web -a <name_of_the_container>`
- Run this command where you have stored the docker file

- If everything is fine, your container will be created successfully

## Release it on the web server 
`Heroku container:release web -a <name_of_the_container>`

- All right all set 

- Next, wondering??
 `http://<name_of_the_container>.herokuapp.com/v1/models/<name_of_model>:predict`
 
