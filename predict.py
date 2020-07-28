import json
import numpy as np
import pickle
import requests

X_test = pickle.load(open("X_test.pickle","rb"))

a = np.array(X_test) 

input_data_json = json.dumps({
    "signature_name":"serving_default",
    "instances":a.tolist()
})


#Request to Local Server when deployed Locally
SERVER_URL = "http://localhost:8501/v1/models/saved_model:predict"
response = requests.post(SERVER_URL,data=input_data_json)
response.raise_for_status()
response = response.json()

y_prob = np.array(response["predictions"])

print(y_prob)


#Request to Remote Server when deployed Remotely
"""
SERVER_URL = "http://saved-model1.herokuapp.com/v1/models/saved_model:predict"
response = requests.post(SERVER_URL,data=input_data_json)
response.raise_for_status()
response = response.json()

"""